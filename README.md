# cca-f-exam-prep
This is Sundar's repository for testing the concepts of CCA
---

## Key Concepts Learned

### Stateless API
Every API call starts completely fresh. Claude has zero memory 
between calls. You must send the full conversation history every 
single time. This is why context management is an entire exam domain.

### stop_reason is everything
```python
if response.stop_reason == "end_turn":
    stop()          # Claude is done

elif response.stop_reason == "tool_use":
    execute_tool()  # Claude needs more info, keep going
```
Never parse Claude's text to decide when to stop. Always use stop_reason.

### Environment Variables
Never hardcode API keys in code. Store in environment variables.
Your code reads the key securely without exposing it.

---

## Study Resources
- [Official Exam Guide](https://anthropic.skilljar.com)
- [Anthropic API Docs](https://platform.claude.com/docs/en/home)
- [Claude Code Docs](https://code.claude.com/docs/en)
- [MCP Official Spec](https://modelcontextprotocol.io)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

---

## Progress

| Exercise | Domain | Task | Status |
|----------|--------|------|--------|
| Agentic loop | Domain 1 | 1.1, 1.2 | ✅ Done |
| Multi-tool loop | Domain 1 | 1.3 | ⬜ Coming |
| Coordinator + subagents | Domain 1 | 1.4, 1.5 | ⬜ Coming |
| Task decomposition | Domain 1 | 1.6 | ⬜ Coming |
| Hooks | Domain 1 | 1.8 | ⬜ Coming |
| Tool design | Domain 2 | 2.1, 2.2 | ⬜ Coming |
| MCP integration | Domain 2 | 2.3 | ⬜ Coming |
| CLAUDE.md | Domain 3 | 3.1, 3.2 | ⬜ Coming |
| Structured output | Domain 4 | 4.2, 4.3 | ⬜ Coming |
| Context management | Domain 5 | 5.1 | ⬜ Coming |

---

*Learning in public — Bengaluru, India 🇮🇳*
*Preparing for CCA-F — Claude Certified Architect Foundations*
