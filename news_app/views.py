from django.shortcuts import render,get_object_or_404
from .models import Category, News
from django.http import Http404


# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Puplished)

    context = {'news_list': news_list}

    return render(request, "news/news_list.html", context=context)


def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Puplished)
    context = {
        'news': news
    }

    return render(request, "news/news_detail.html", context=context)


def HomePageView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:3]
    local_1 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[1]
    local_2 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[2]
    local_3 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[3]
    local_4 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[4]
    local_5 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[5]
    local_6 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[6]
    local_7 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[7]
    local_8 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[8]
    local_9 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[9]
    local_10 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[10]
    local_11 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[11]
    local_12 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[12]
    local_13 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[13]
    local_14 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[14]
    local_15 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[15]
    local_16 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[16]
    local_17 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[17]
    local_18 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[18]
    sport_1 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[1]
    sport_2 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[2]
    sport_3 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[3]
    sport_4 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[4]
    sport_5 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[5]
    sport_6 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[6]
    sport_7 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[7]
    sport_8 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[8]
    sport_9 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[9]
    sport_10 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[10]
    sport_11 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[11]
    sport_12 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[12]
    sport_13 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[13]
    sport_14 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[14]
    sport_15 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[15]
    sport_16 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[16]
    sport_17 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[17]
    sport_18 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[18]
    jahon_one = News.published.all().filter(category__name="Jahon").order_by("-publish_time")
    qiziqarli_yangilik = News.published.all().filter(category__name="Qiziqarli_yangilik").order_by("-publish_time")
    avtomabil1 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[1]
    avtomabil2 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[2]
    avtomabil3 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[3]
    avtomabil4 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[4]
    avtomabil5 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[5]
    avtomabil6 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[6]
    avtomabil7 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[7]
    avtomabil8 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[8]
    avtomabil9 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[9]
    avtomabil10 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[10]
    avtomabil11 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[11]
    avtomabil12 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[12]
    avtomabil13 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[13]
    avtomabil14 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[14]
    avtomabil15 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[15]
    avtomabil16 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[16]
    avtomabil17 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[17]
    avtomabil18 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[18]
    jahon1 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[0]
    jahon2 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[1]
    jahon3 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[2]
    jahon4 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[3]
    jahon5 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[4]
    jahon6 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[5]
    jahon7 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[6]
    jahon8 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[7]
    jahon9 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[8]
    jahon10 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[9]
    jahon11 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[10]
    jahon12 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[11]
    jahon13 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[12]
    jahon14 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[13]
    jahon15 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[14]
    jahon16 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[15]
    jahon17 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[16]
    jahon18 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[17]
    iqtisodiyot1 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[0]
    iqtisodiyot2 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[1]
    iqtisodiyot3 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[2]
    iqtisodiyot4 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[3]
    iqtisodiyot5 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[4]
    iqtisodiyot6 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[5]
    iqtisodiyot7 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[6]
    iqtisodiyot8 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[7]
    iqtisodiyot9 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[8]
    iqtisodiyot10 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[9]
    iqtisodiyot11 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[10]
    iqtisodiyot12 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[11]
    iqtisodiyot13 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[12]
    iqtisodiyot14 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[13]
    iqtisodiyot15 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[14]
    iqtisodiyot16 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[15]
    iqtisodiyot17 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[16]
    iqtisodiyot18 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[17]

    context = {
        "news_list": news_list,
        "categories": categories,
        "local_1": local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "local_5": local_5,
        "local_6": local_6,
        "local_7": local_7,
        "local_8": local_8,
        "local_9": local_9,
        "local_10": local_10,
        "local_11": local_11,
        "local_12": local_12,
        "local_13": local_13,
        "local_14": local_14,
        "local_15": local_15,
        "local_16": local_16,
        "local_17": local_17,
        "local_18": local_18,
        "jahon_one": jahon_one,
        "sport_1": sport_1,
        "sport_2": sport_2,
        "sport_3": sport_3,
        "sport_4": sport_4,
        "sport_5": sport_5,
        "sport_6": sport_6,
        "sport_7": sport_7,
        "sport_8": sport_8,
        "sport_9": sport_9,
        "sport_10": sport_10,
        "sport_11": sport_11,
        "sport_12": sport_12,
        "sport_13": sport_13,
        "sport_14": sport_14,
        "sport_15": sport_15,
        "sport_16": sport_16,
        "sport_17": sport_17,
        "sport_18": sport_18,
        "qiziqarli_yangilik": qiziqarli_yangilik,
        "avtomabil1": avtomabil1,
        "avtomabil2": avtomabil2,
        "avtomabil3": avtomabil3,
        "avtomabil4": avtomabil4,
        "avtomabil5": avtomabil5,
        "avtomabil6": avtomabil6,
        "avtomabil7": avtomabil7,
        "avtomabil8": avtomabil8,
        "avtomabil9": avtomabil9,
        "avtomabil10": avtomabil10,
        "avtomabil11": avtomabil11,
        "avtomabil12": avtomabil12,
        "avtomabil13": avtomabil13,
        "avtomabil14": avtomabil14,
        "avtomabil15": avtomabil15,
        "avtomabil16": avtomabil16,
        "avtomabil17": avtomabil17,
        "avtomabil18": avtomabil18,
        "jahon1": jahon1,
        "jahon2": jahon2,
        "jahon3": jahon3,
        "jahon4": jahon4,
        "jahon5": jahon5,
        "jahon6": jahon6,
        "jahon7": jahon7,
        "jahon8": jahon8,
        "jahon9": jahon9,
        "jahon10": jahon10,
        "jahon11": jahon11,
        "jahon12": jahon12,
        "jahon13": jahon13,
        "jahon14": jahon14,
        "jahon15": jahon15,
        "jahon16": jahon16,
        "jahon17": jahon17,
        "jahon18": jahon18,
        "iqtisodiyot1": iqtisodiyot1,
        "iqtisodiyot2": iqtisodiyot2,
        "iqtisodiyot3": iqtisodiyot3,
        "iqtisodiyot4": iqtisodiyot4,
        "iqtisodiyot5": iqtisodiyot5,
        "iqtisodiyot6": iqtisodiyot6,
        "iqtisodiyot7": iqtisodiyot7,
        "iqtisodiyot8": iqtisodiyot8,
        "iqtisodiyot9": iqtisodiyot9,
        "iqtisodiyot10": iqtisodiyot10,
        "iqtisodiyot11": iqtisodiyot11,
        "iqtisodiyot12": iqtisodiyot12,
        "iqtisodiyot13": iqtisodiyot13,
        "iqtisodiyot14": iqtisodiyot14,
        "iqtisodiyot15": iqtisodiyot15,
        "iqtisodiyot16": iqtisodiyot16,
        "iqtisodiyot17": iqtisodiyot17,
        "iqtisodiyot18": iqtisodiyot18,

    }

    return render(request, 'news/index.html', context)


def UzbekPage(request):
    local_1 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[1]
    local_2 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[2]
    local_3 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[3]
    local_4 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[4]
    local_5 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[5]
    local_6 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[6]
    local_7 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[7]
    local_8 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[8]
    local_9 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[9]
    local_10 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[10]
    local_11 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[11]
    local_12 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[12]
    local_13 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[13]
    local_14 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[14]
    local_15 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[15]
    local_16 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[16]
    local_17 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[17]
    local_18 = News.published.all().filter(category__name="Uzbekiston").order_by("-publish_time")[18]
    context = {
        "local_1": local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "local_5": local_5,
        "local_6": local_6,
        "local_7": local_7,
        "local_8": local_8,
        "local_9": local_9,
        "local_10": local_10,
        "local_11": local_11,
        "local_12": local_12,
        "local_13": local_13,
        "local_14": local_14,
        "local_15": local_15,
        "local_16": local_16,
        "local_17": local_17,
        "local_18": local_18,
    }
    return render(request, 'news/uzbekistan.html', context)


def SportPage(request):
    sport_1 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[1]
    sport_2 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[2]
    sport_3 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[3]
    sport_4 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[4]
    sport_5 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[5]
    sport_6 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[6]
    sport_7 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[7]
    sport_8 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[8]
    sport_9 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[9]
    sport_10 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[10]
    sport_11 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[11]
    sport_12 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[12]
    sport_13 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[13]
    sport_14 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[14]
    sport_15 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[15]
    sport_16 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[16]
    sport_17 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[17]
    sport_18 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[18]
    context = {
        "sport_1": sport_1,
        "sport_2": sport_2,
        "sport_3": sport_3,
        "sport_4": sport_4,
        "sport_5": sport_5,
        "sport_6": sport_6,
        "sport_7": sport_7,
        "sport_8": sport_8,
        "sport_9": sport_9,
        "sport_10": sport_10,
        "sport_11": sport_11,
        "sport_12": sport_12,
        "sport_13": sport_13,
        "sport_14": sport_14,
        "sport_15": sport_15,
        "sport_16": sport_16,
        "sport_17": sport_17,
        "sport_18": sport_18,
    }
    return render(request, 'news/sport.html', context)


def AvtomabilPage(request):
    avtomabil1 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[1]
    avtomabil2 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[2]
    avtomabil3 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[3]
    avtomabil4 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[4]
    avtomabil5 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[5]
    avtomabil6 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[6]
    avtomabil7 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[7]
    avtomabil8 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[8]
    avtomabil9 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[9]
    avtomabil10 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[10]
    avtomabil11 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[11]
    avtomabil12 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[12]
    avtomabil13 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[13]
    avtomabil14 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[14]
    avtomabil15 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[15]
    avtomabil16 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[16]
    avtomabil17 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[17]
    avtomabil18 = News.published.all().filter(category__name="Avtomabil").order_by("-publish_time")[18]
    context = {
        "avtomabil1": avtomabil1,
        "avtomabil2": avtomabil2,
        "avtomabil3": avtomabil3,
        "avtomabil4": avtomabil4,
        "avtomabil5": avtomabil5,
        "avtomabil6": avtomabil6,
        "avtomabil7": avtomabil7,
        "avtomabil8": avtomabil8,
        "avtomabil9": avtomabil9,
        "avtomabil10": avtomabil10,
        "avtomabil11": avtomabil11,
        "avtomabil12": avtomabil12,
        "avtomabil13": avtomabil13,
        "avtomabil14": avtomabil14,
        "avtomabil15": avtomabil15,
        "avtomabil16": avtomabil16,
        "avtomabil17": avtomabil17,
        "avtomabil18": avtomabil18,
    }
    return render(request, 'news/avtomabil.html', context)


def JahonPage(request):
    jahon1 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[0]
    jahon2 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[1]
    jahon3 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[2]
    jahon4 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[3]
    jahon5 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[4]
    jahon6 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[5]
    jahon7 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[6]
    jahon8 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[7]
    jahon9 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[8]
    jahon10 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[9]
    jahon11 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[10]
    jahon12 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[11]
    jahon13 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[12]
    jahon14 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[13]
    jahon15 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[14]
    jahon16 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[15]
    jahon17 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[16]
    jahon18 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[17]
    context = {
        "jahon1": jahon1,
        "jahon2": jahon2,
        "jahon3": jahon3,
        "jahon4": jahon4,
        "jahon5": jahon5,
        "jahon6": jahon6,
        "jahon7": jahon7,
        "jahon8": jahon8,
        "jahon9": jahon9,
        "jahon10": jahon10,
        "jahon11": jahon11,
        "jahon12": jahon12,
        "jahon13": jahon13,
        "jahon14": jahon14,
        "jahon15": jahon15,
        "jahon16": jahon16,
        "jahon17": jahon17,
        "jahon18": jahon18,
    }
    return render(request, 'news/jahon.html', context)


def IqtisodPage(request):
    iqtisodiyot1 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[0]
    iqtisodiyot2 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[1]
    iqtisodiyot3 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[2]
    iqtisodiyot4 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[3]
    iqtisodiyot5 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[4]
    iqtisodiyot6 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[5]
    iqtisodiyot7 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[6]
    iqtisodiyot8 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[7]
    iqtisodiyot9 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[8]
    iqtisodiyot10 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[9]
    iqtisodiyot11 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[10]
    iqtisodiyot12 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[11]
    iqtisodiyot13 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[12]
    iqtisodiyot14 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[13]
    iqtisodiyot15 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[14]
    iqtisodiyot16 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[15]
    iqtisodiyot17 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[16]
    iqtisodiyot18 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[17]
    context = {
        "iqtisodiyot1": iqtisodiyot1,
        "iqtisodiyot2": iqtisodiyot2,
        "iqtisodiyot3": iqtisodiyot3,
        "iqtisodiyot4": iqtisodiyot4,
        "iqtisodiyot5": iqtisodiyot5,
        "iqtisodiyot6": iqtisodiyot6,
        "iqtisodiyot7": iqtisodiyot7,
        "iqtisodiyot8": iqtisodiyot8,
        "iqtisodiyot9": iqtisodiyot9,
        "iqtisodiyot10": iqtisodiyot10,
        "iqtisodiyot11": iqtisodiyot11,
        "iqtisodiyot12": iqtisodiyot12,
        "iqtisodiyot13": iqtisodiyot13,
        "iqtisodiyot14": iqtisodiyot14,
        "iqtisodiyot15": iqtisodiyot15,
        "iqtisodiyot16": iqtisodiyot16,
        "iqtisodiyot17": iqtisodiyot17,
        "iqtisodiyot18": iqtisodiyot18,
    }
    return render(request, 'news/iqtisodiyot.html', context)