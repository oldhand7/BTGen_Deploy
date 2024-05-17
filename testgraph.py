import requests

try:
    callback_payload_images = [{'url': 'http://204.12.253.115:9999/files/2024-05-16/5a799083-f50f-4c41-94cf-e7f76176d7ce.png', 'prompt': 'Preppy Beautiful girl at a beautiful New New York Restaurant In a trendy and stylish interior with artistic decor, a lively energy.'}, {'url': 'http://204.12.253.115:9999/files/2024-05-16/665b70b5-ea4c-4ed9-b391-0ca2d0c5143f.png', 'prompt': 'Preppy model smiles in a beautiful fashion photo in Paris in Spring, where Haussmann-style buildings line tree-lined boulevards, the Eiffel Tower looms in the distance, and the Seine flows under bridges.'}, {'url': 'http://204.12.253.115:9999/files/2024-05-16/3b0ceccd-f6b2-41ae-818c-dc06e57f70f6.png', 'prompt': 'Preppy Beautiful guest at a beautiful semi-formal wedding: at a an elegant botanical garden, surrounded by lush greenery and vibrant blooms.'}]
    graphql_request = {
        "query": "mutation UpdateImagesGeneration($data: ImageGenerationInput!) { updateImagesGeneration(data: $data) { status }}",
        "variables": {
            "data": {
            
                "images":callback_payload_images,
                "isUserInput": False
            }
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer " ,
        "Cookie": "jgb_cs=s%3A96Q5_rfHS3EaRCEV6iKlsX7u_zm4naZD.yKB%2BJ35mmaGGryviAAagXeCrvkyAC9K4rCLjc4Xzd8c"
    }

    # Define the GraphQL API endpoint for staging
    print(" ------------------ before request to graphql -----------")
    url = "https://stage-graphql.beautifultechnologies.app/"
    #Define the GraphQL API endpoint for production
    # url = "https://graphql.beautifultechnologies.app/"

    # Send the HTTP request using the `requests` library
    response = requests.post(url, json=graphql_request, headers=headers)
    print("after request")
    print(" -----------  resopnse ------------", response)
    print(response.content)
    print(response.status_code)
    
except Exception as e:
    print(e)
