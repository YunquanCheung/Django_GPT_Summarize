#from django.shortcuts import render,HttpResponse
from django.views import View
import openai
from init import GPT_KEY, GPT_MODELS,TEXT_LENG
from gptapi.models import SUMMARIZES
from django.http import JsonResponse
# Create your views here.

def text_leng(text):
    """
    对文本进行筛选
    """
    if 0<len(text)<=TEXT_LENG:
        leng_status = True
    else:
        leng_status = False
    return leng_status
class GPT_API(View):
    def post(self, request):
        results = {"code": 404, "status": "handle error"}
        
        try:
            input_text = request.POST.get("text")
            
            if not input_text:
                raise ValueError("Text is missing!")
                
            if not text_leng(input_text):
                raise ValueError("There is an error in the text length!")
            
            reply_content = get_openai_reply(input_text)
            
            store_in_database(input_text, reply_content)
            
            results = {"code": 200, "status": "success", "summary": reply_content}
        
        except Exception as e:
            results["error"] = str(e)
    
        return JsonResponse(results)
    
    def get_openai_reply(input_text):
        openai.api_key = GPT_KEY
        input_text = "Write a concise and comprehensive summary of [" + input_text + "]"
        message_history = [{"role": "user", "content": input_text}]
        
        completion = openai.ChatCompletion.create(
            model=GPT_MODELS,
            messages=message_history,
        )
        
        return completion.choices[0].message.content
    
    def store_in_database(input_text, reply_content):
        SUMMARIZES.objects.create(input_text=input_text, summary=reply_content)

