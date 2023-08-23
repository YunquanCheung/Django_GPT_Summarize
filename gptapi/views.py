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
    def get(self,request):
        results = {"code": 404, "status": "handle error"}
        return JsonResponse(results)

    def post(self,request):
        results = {"code": 404, "status": "handle error"}
        try:
            input_text = request.POST.get("text")
            if text_leng(input_text):
                openai.api_key = GPT_KEY
                message_histoty = []
                message_histoty.append({"role": "user", "content": input_text})
                completion = openai.ChatCompletion.create(
                    # model="gpt-3.5-turbo",
                    model=GPT_MODELS,
                    messages=message_histoty,
                )
                reply_content = completion.choices[0].message.content
                print("Answers: " + reply_content)
                message_histoty.append({"role": "assistant", "content": reply_content})
                SUMMARIZES.objects.create(input_text=input_text,summary=reply_content)
                results = {"code": 200, "status": "success", "summary": reply_content}
            else:
                results["error"] = "There is an error in the text length!"
        except Exception as e:
            results["error"] = str(e)
        return JsonResponse(results)

