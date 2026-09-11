// dsh skill plugin — registers every SKILL.md under skills/ (recursive) as a dsh skill.
import { readFileSync, readdirSync, statSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { join } from 'node:path'

const skillsDir = fileURLToPath(new URL('./skills/', import.meta.url))

export const name = 'marketing-skills'

function walk(dir, out = []) {
  for (const entry of readdirSync(dir)) {
    const p = join(dir, entry)
    if (statSync(p).isDirectory()) walk(p, out)
    else if (entry === 'SKILL.md') out.push(p)
  }
  return out
}

function parseFrontmatter(md) {
  const m = md.match(/^---\n([\s\S]*?)\n---\n/)
  if (!m) return {}
  const fm = m[1]
  const name = fm.match(/^name:\s*(\S+)/m)?.[1]
  const line = fm.split('\n').find((l) => l.startsWith('description:'))
  let desc = line ? line.replace(/^description:\s*/, '').trim() : ''
  if ((desc.startsWith('"') && desc.endsWith('"')) || (desc.startsWith("'") && desc.endsWith("'"))) {
    desc = desc.slice(1, -1).replace(/\\"/g, '"').replace(/\\n/g, '\n')
  }
  const content = md.replace(/^---\n[\s\S]*?\n---\n/, '').trim()
  return { name, desc, content }
}

export function apply(ctx) {
  let n = 0
  for (const file of walk(skillsDir)) {
    try {
      const raw = readFileSync(file, 'utf8')
      const { name, desc, content } = parseFrontmatter(raw)
      if (name && desc && content) {
        ctx.skills.register({ name, description: desc, source: 'runtime', content })
        n++
      }
    } catch (e) {
      // skip unreadable/non-skill files
    }
  }
  console.log(`[marketing-skills] registered ${n} skills`)
}
