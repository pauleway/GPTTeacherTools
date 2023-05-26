 async function getPromptResponse(prompt, temp = 0.7, max_tokens = 300) {
     let response = await fetch("/get-prompt-response?" + new URLSearchParams({
         "prompt": prompt,
         "temp":temp,
         "max_tokens":max_tokens
     }))
     return response
 }

