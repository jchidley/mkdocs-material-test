#!/bin/bash
# Check latest posts from pragmatic AI/programming blogs
# Requires: brave-search skill configured

SKILL_DIR="$HOME/.codex/skills/brave-search"

blogs=(
    "sebastianraschka.com/blog"
    "karpathy.ai"
    "fast.ai"
    "hamel.dev"
    "jvns.ca"
    "huyenchip.com/blog"
    "eugeneyan.com"
    "vickiboykis.com"
    "lilianweng.github.io"
    "jalammar.github.io"
    "aisnakeoil.com"
    "swyx.io"
    "mitchellh.com"
    "rachel.fast.ai"
    "simonwillison.net"
    "mariozechner.at"
    "lucumr.pocoo.org"
)

echo "# Blog Update Check - $(date '+%Y-%m-%d')"
echo ""
echo "| Blog | Latest Post | Age |"
echo "|------|-------------|-----|"

for blog in "${blogs[@]}"; do
    result=$("$SKILL_DIR/search.js" "site:$blog" -n 1 2>/dev/null)
    title=$(echo "$result" | grep "^Title:" | sed 's/Title: //')
    age=$(echo "$result" | grep "^Age:" | sed 's/Age: //')
    echo "| $blog | ${title:-N/A} | ${age:-N/A} |"
    sleep 0.5  # Rate limiting
done
