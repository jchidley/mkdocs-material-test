#!/usr/bin/env node
/**
 * Check latest posts from pragmatic AI/programming blogs
 * Usage: node check-blogs.js
 * 
 * Requires: brave-search skill configured with BRAVE_API_KEY
 */

const { execSync } = require('child_process');
const path = require('path');

const BRAVE_SKILL = path.join(process.env.HOME, '.codex/skills/brave-search');

const blogs = [
  // Tier 1
  { name: 'Simon Willison', url: 'simonwillison.net', tier: 1 },
  { name: 'Mario Zechner', url: 'mariozechner.at', tier: 1 },
  { name: 'Armin Ronacher', url: 'lucumr.pocoo.org', tier: 1 },
  { name: 'Sebastian Raschka', url: 'sebastianraschka.com/blog', tier: 1 },
  { name: 'Andrej Karpathy', url: 'karpathy.ai', tier: 1 },
  { name: 'Jeremy Howard', url: 'answer.ai', tier: -1 },
  { name: 'Hamel Husain', url: 'hamel.dev', tier: 1 },
  { name: 'Julia Evans', url: 'jvns.ca', tier: 1 },
  { name: 'Dan Luu', url: 'danluu.com', tier: 1 },
  { name: 'Rachel Kroll', url: 'rachelbythebay.com', tier: 1 },
  { name: 'Xe Iaso', url: 'xeiaso.net', tier: 1 },
  { name: 'Filippo Valsorda', url: 'words.filippo.io', tier: 1 },
  { name: 'Lexi Mattick', url: 'cpu.land', tier: 1 },
  { name: 'Hillel Wayne', url: 'hillelwayne.com', tier: 1 },
  { name: 'Peter Steinberger', url: 'steipete.me', tier: 1 },
  { name: 'Geoffrey Huntley', url: 'ghuntley.com', tier: 1 },
  { name: 'Amos Wenger', url: 'fasterthanli.me', tier: 1 },
  // Tier 2
  { name: 'Chip Huyen', url: 'huyenchip.com', tier: 2 },
  { name: 'Eugene Yan', url: 'eugeneyan.com', tier: 2 },
  { name: 'Vicki Boykis', url: 'vickiboykis.com', tier: 2 },
  { name: 'Lilian Weng', url: 'lilianweng.github.io', tier: 2 },
  { name: 'Jay Alammar', url: 'jalammar.github.io', tier: 2 },
  // Tier 3
  { name: 'AI Snake Oil', url: 'aisnakeoil.com', tier: 3 },
  { name: 'swyx', url: 'swyx.io', tier: 3 },
  { name: 'Mitchell Hashimoto', url: 'mitchellh.com', tier: 3 },
  { name: 'Rachel Thomas', url: 'rachel.fast.ai', tier: 3 },

  // Legendary
  { name: 'Fabrice Bellard', url: 'bellard.org', tier: -1 },
];

function searchBlog(blog) {
  try {
    const cmd = `"${BRAVE_SKILL}/search.js" "site:${blog.url}" -n 1 --freshness py`;
    const result = execSync(cmd, { encoding: 'utf8', timeout: 30000, stdio: ['pipe', 'pipe', 'pipe'] });
    
    const titleMatch = result.match(/^Title: (.+)$/m);
    const ageMatch = result.match(/^Age: (.+)$/m);
    
    return {
      name: blog.name,
      url: blog.url,
      tier: blog.tier,
      title: titleMatch ? titleMatch[1].substring(0, 60) : 'N/A',
      age: ageMatch ? ageMatch[1] : 'N/A'
    };
  } catch (e) {
    return {
      name: blog.name,
      url: blog.url,
      tier: blog.tier,
      title: 'Error fetching',
      age: 'N/A'
    };
  }
}

async function main() {
  const date = new Date().toISOString().split('T')[0];
  
  console.log(`# Blog Update Check - ${date}\n`);
  
  const tiers = {
    '-1': '## Builders First, Writers Second',
    1: '## Tier 1: Highly Recommended',
    2: '## Tier 2: Excellent',
    3: '## Tier 3: Worth Following'
  };
  
  const results = [];
  
  for (const blog of blogs) {
    process.stderr.write(`Checking ${blog.name}...\n`);
    const result = searchBlog(blog);
    results.push(result);
    // Rate limiting
    await new Promise(r => setTimeout(r, 500));
  }
  
  // Group by tier
  for (const tier of [-1, 1, 2, 3]) {
    const tierResults = results.filter(r => r.tier === tier);
    if (tierResults.length === 0) continue;
    
    console.log(`\n${tiers[tier]}\n`);
    console.log('| Person | Blog | Latest | Age |');
    console.log('|--------|------|--------|-----|');
    
    for (const r of tierResults) {
      console.log(`| ${r.name} | [${r.url}](https://${r.url}) | ${r.title} | ${r.age} |`);
    }
  }
}

main().catch(console.error);
