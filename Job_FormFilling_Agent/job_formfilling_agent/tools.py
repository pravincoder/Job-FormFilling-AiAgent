from crewai_tools import WebsiteSearchTool

# Example of initiating tool that agents can use 
# to search across any discovered websites
def website_search_tool():
    tool =  WebsiteSearchTool(
        config=dict(
            llm=dict(
                provider="ollama", # or google, openai, anthropic, llama2, ...
                config=dict(
                    model="llama3.2:1b ",
                    # temperature=0.5,
                    # top_p=1,
                    # stream=true,
                ),
            ),
            embedder=dict(
                provider="ollama", # or openai, ollama, ...
                config=dict(
                    model="nomic-embed-text",
                    # title="Embeddings",
                ),
            ),
        )
    )
    return tool
