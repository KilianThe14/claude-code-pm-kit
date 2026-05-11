#!/usr/bin/env bash
set -euo pipefail

CLAUDE_HOME="${CLAUDE_HOME:-$HOME/.claude}"
missing=0

require_path() {
  local rel="$1"
  if [[ ! -e "$CLAUDE_HOME/$rel" ]]; then
    echo "missing: $rel"
    missing=1
  else
    echo "ok: $rel"
  fi
}

require_path "CLAUDE.md"
require_path "skills/pm-prd/SKILL.md"
require_path "skills/pm-discovery/SKILL.md"
require_path "skills/pm-prioritization/SKILL.md"
require_path "skills/pm-competitive-analysis/SKILL.md"
require_path "skills/pm-meeting-synthesis/SKILL.md"
require_path "skills/pm-review/SKILL.md"
require_path "skills/pm-launch-retro/SKILL.md"
require_path "skills/pm-stakeholder-update/SKILL.md"
require_path "skills/pm-experiment-design/SKILL.md"
require_path "skills/pm-user-story-mapping/SKILL.md"
require_path "skills/product-management/SKILL.md"
require_path "skills/discovery-process/SKILL.md"
require_path "skills/problem-definition/SKILL.md"
require_path "skills/conducting-user-interviews/SKILL.md"
require_path "skills/analyzing-user-feedback/SKILL.md"
require_path "skills/prd-development/SKILL.md"
require_path "skills/prioritizing-roadmap/SKILL.md"
require_path "skills/setting-okrs-goals/SKILL.md"
require_path "skills/stakeholder-alignment/SKILL.md"
require_path "skills/shipping-products/SKILL.md"
require_path "commands/prd.md"
require_path "commands/review-prd.md"
require_path "commands/research-plan.md"
require_path "commands/analyze-interviews.md"
require_path "commands/prioritize.md"
require_path "commands/competitive-analysis.md"
require_path "commands/meeting-notes.md"
require_path "commands/launch-checklist.md"
require_path "commands/stakeholder-update.md"
require_path "commands/experiment-plan.md"
require_path "templates/standard-prd.md"
require_path "templates/light-prd.md"
require_path "templates/requirements-clarification.md"
require_path "templates/user-interview.md"
require_path "templates/competitive-analysis.md"
require_path "templates/prioritization-scorecard.md"
require_path "templates/experiment-design.md"
require_path "templates/launch-retro.md"
require_path "scripts/rice_prioritizer.py"
require_path "scripts/interview_synthesizer.py"

if [[ "$missing" -ne 0 ]]; then
  echo "Healthcheck failed for $CLAUDE_HOME"
  exit 1
fi

echo "Claude Code PM Kit healthcheck passed for $CLAUDE_HOME"
