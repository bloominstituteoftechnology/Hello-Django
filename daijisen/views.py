from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import urllib
import requests
import re


def index(request):
    return HttpResponse("Hello, world. You're at the Daijisen index.")


def word(request, word):
    r = requests.get('https://kotobank.jp/word/' + word)

    daijisenRegex = r'デジタル大辞泉<\/a>([^\r]*?)(?=<!-- \/\.dictype 辞書ひとつ -->)'
    daijirinRegex = r'大辞林 第三版<\/a>([^\r]*?)(?=<!-- \/\.dictype 辞書ひとつ -->)'

    replaceHeaderRegex = r'[^!]*<\/h2>'
    replaceSourceRegex = r'<p class=\"source\">([^\r]*?)(<!-- \/\.source -->)'

    pattern = re.compile(daijisenRegex)
    daijisenDefinition = re.compile(daijisenRegex).search(r.text)
    daijirinDefinition = re.compile(daijirinRegex).search(r.text)

    removeKanjiKoumokuRegex = r'<div class="ex cf">[\n 	]*<h3>([^［<]*?)［漢字項目］([^\r]*?)<!-- \/\.ex 解説 -->'
    removeNonDefinitions = r'<div class="ex cf">[\n 	]*<h3>([^［<]*?)［([^\r]*?)<!-- \/\.ex 解説 -->'

    result = ""

    if (daijisenDefinition):
        result += re.sub(replaceHeaderRegex,
                         "<article id='daijisen' class='definition'><h2>大辞泉</h2>", daijisenDefinition.group())

    if (daijirinDefinition):
        result += re.sub(replaceHeaderRegex,
                         "<article id='daijirin' class='definition'><h2>大辞林</h2>", daijirinDefinition.group())

    result = re.sub(replaceSourceRegex, '', result, flags=re.IGNORECASE)
    result = re.sub(r'\n', '', result)
    result = re.sub(r'\/word\/', '/daijisen/word/', result)

    return HttpResponse(result)
