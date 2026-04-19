#!/bin/bash
# claude-doctor-continuous.sh
#
# Stop hook: At end of each turn, run claude-doctor to detect anti-patterns and emit rule candidates.
# Throttling (10 minutes) and background execution avoid impacting Claude Code UX.
#
# Operations workflow:
#   1. While you work, the hook quietly accumulates reports in the background
#   2. Periodically inspect the latest report: ls -lt ~/.claude/claude-doctor-reports/ | head
#   3. Pick rules to adopt and append them to ~/.claude/CLAUDE.md or each project's CLAUDE.md
#   4. Remove old reports: find ~/.claude/claude-doctor-reports -mtime +30 -delete

# Discard stdin so the hook runtime does not wait for the pipe to close
cat > /dev/null

LAST_RUN_FILE="$HOME/.claude/.cache/claude-doctor-last-run"
REPORTS_DIR="$HOME/.claude/claude-doctor-reports"

# Ensure directories exist
mkdir -p "$(dirname "$LAST_RUN_FILE")" "$REPORTS_DIR" || true

# Skip if we already ran within the last 10 minutes
if [ -f "$LAST_RUN_FILE" ] && find "$LAST_RUN_FILE" -mmin -10 2>/dev/null | grep -q .; then
  exit 0
fi

# Record run time for the next throttle check
touch "$LAST_RUN_FILE" || true

# Output paths with timestamp
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
REPORT_JSON="$REPORTS_DIR/${TIMESTAMP}.json"
REPORT_LOG="$REPORTS_DIR/${TIMESTAMP}.log"

# Run claude-doctor in the background (close stdin for full detachment)
{
  timeout 120 npx -y claude-doctor@latest --rules --save --json \
    > "$REPORT_JSON" \
    2> "$REPORT_LOG" \
    || true
} </dev/null &
disown

exit 0
