import anthropic
import json
import os
# ── Setup ──────────────────────────────────────────────────────────────────

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# ── Tool Definition ────────────────────────────────────────────────────────
tools = [
    {
        "name": "get_portfolio",
        "description": "Get the current stock portfolio for a Zerodha user. Returns holdings with quantity and current value.",
        "input_schema": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string",
                    "description": "The Zerodha user ID"
                }
            },
            "required": ["user_id"]
        }
    }
]

# ── Mock Tool Execution ────────────────────────────────────────────────────
def execute_tool(tool_name, tool_input):
    print(f"\n🔧 TOOL CALLED: {tool_name}")
    print(f"   Input: {tool_input}")
    
    if tool_name == "get_portfolio":
        result = {
            "user_id": tool_input["user_id"],
            "holdings": [
                {"symbol": "INFY", "quantity": 10, "current_value": 18500},
                {"symbol": "TCS",  "quantity": 5,  "current_value": 21000},
                {"symbol": "HDFC", "quantity": 8,  "current_value": 13600},
            ],
            "total_value": 53100
        }
        print(f"   Result: {result}")
        return result
    
    return {"error": "Unknown tool"}

# ── The Agentic Loop ───────────────────────────────────────────────────────
def run_agentic_loop(user_question):
    print(f"\n{'='*60}")
    print(f"USER: {user_question}")
    print(f"{'='*60}")
    
    messages = [
        {"role": "user", "content": user_question}
    ]
    
    iteration = 0
    max_iterations = 10  # Safety cap
    
    while iteration < max_iterations:
        iteration += 1
        print(f"\n── Loop iteration {iteration} ──")
        
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1000,
            tools=tools,
            messages=messages
        )
        
        print(f"⚡ stop_reason: {response.stop_reason}")
        
        if response.stop_reason == "end_turn":
            final_response = response.content[0].text
            print(f"\n✅ FINAL RESPONSE:\n{final_response}")
            return final_response
        
        elif response.stop_reason == "tool_use":
            messages.append({
                "role": "assistant",
                "content": response.content
            })
            
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = execute_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result)
                    })
            
            messages.append({
                "role": "user",
                "content": tool_results
            })
        
        else:
            print(f"⚠️ Unexpected stop_reason: {response.stop_reason}")
            break
    
    print("⚠️ Hit max iterations safety cap")

# ── Run It ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    run_agentic_loop("What is the current value of my Zerodha portfolio? My user ID is ZR1234.")
    # run_agentic_loop("What is the current Whether in Bangalore")