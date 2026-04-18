documents = {
  "morocco overview": "morocco is a north african country known for its rich cultural heritage and diverse landscapes\nit blends arab berber and european influences in daily life and traditions\nthe country includes mountains deserts and coastlines which makes it geographically unique\nmorocco continues to grow while preserving its identity and cultural roots",

  "morocco culture": "moroccan culture is a mix of arab amazigh and african traditions\nthis diversity appears in music clothing and daily lifestyle\ntraditional crafts like carpets and tiles reflect strong artistic heritage\nfood and social gatherings play an important role in community life",

  "morocco economy": "morocco has a developing economy based on agriculture tourism and industry\nkey exports include phosphates textiles and agricultural products\nmajor cities act as economic centers attracting investment\nthe country is working to improve growth and reduce inequality",

  "tourism in morocco": "tourism is a major sector that attracts millions of visitors each year\ntravelers explore cities deserts and coastal areas\nthe government invests in infrastructure to support tourism growth\nsustainability is becoming important to protect natural and cultural assets",

  "desert tourism": "the sahara desert is one of the most popular attractions in morocco\nvisitors enjoy camel rides and overnight stays in camps\nthe experience includes peaceful landscapes and unique views\nlocal communities benefit from tourism activities in desert regions",

  "city tourism": "moroccan cities combine traditional and modern lifestyles\nold medina areas offer markets architecture and history\nmodern districts provide shopping dining and business spaces\nthis mix creates a rich and dynamic experience for visitors",

  "football in morocco": "football is the most popular sport in morocco\nit plays a strong role in national pride and unity\nthe national team has gained international recognition\nlocal clubs also contribute to the development of the sport",

  "football strategy": "football strategy focuses on planning tactics to win matches\nteams use formations positioning and movement to control the game\ncoaches study opponents to adapt their approach\nteam coordination is essential for success on the field",

  "team dynamics": "team dynamics are important for performance and success\nplayers need trust and communication with each other\nleadership helps guide the team and maintain discipline\nstrong teamwork often leads to better results than individual talent",

  "tourism strategy": "tourism strategy aims to attract and retain visitors\nit includes marketing infrastructure and service quality\ncountries invest in branding to improve their global image\ngood experiences encourage visitors to return again",

  "business strategy": "business strategy defines how organizations reach their goals\nit involves planning execution and evaluation of actions\ncompanies analyze markets to stay competitive\nadaptability is important in changing environments",

  "morocco tourism strategy": "morocco focuses on increasing tourism and improving quality\ninvestment in infrastructure supports this growth\ncultural preservation is part of the strategy\nthe goal is sustainable and long term development",

  "morocco football development": "morocco invests in developing young football talent\ntraining centers and academies are improving\ninternational success motivates new generations\nthe focus is on long term progress and performance",

  "sports tourism": "sports tourism combines travel with sports events and activities\nfootball events attract international visitors to morocco\nfans travel to support teams and explore new places\nthis sector contributes to economic growth",

  "strategic planning": "strategic planning helps define goals and actions\norganizations analyze risks and opportunities\nplans are implemented and adjusted when needed\nthis process improves decision making and results",

  "morocco global positioning": "morocco acts as a bridge between africa and europe\nits location supports trade and tourism activities\nthe country builds international partnerships\nit works to strengthen its global presence and influence",

  "tourism experience": "tourism experience focuses on visitor satisfaction\nit includes services interactions and emotions\npositive experiences lead to recommendations\npersonalized travel is becoming more important",

  "football analytics": "football analytics uses data to improve performance\nteams study player statistics and match behavior\ntechnology helps collect and analyze information\ndata driven decisions improve competitive advantage",

  "integrated strategy morocco tourism football": "combining tourism and football creates strong opportunities\nevents attract global attention and visitors\nfootball success helps promote the country image\ncoordination between sectors increases impact",

  "future vision morocco strategy": "morocco focuses on sustainable growth and innovation\ninvestment in technology supports development\ntourism and sports remain key sectors\nthe vision aims for long term success and stability"
}

import math
from collections import defaultdict, Counter

def calculate_tf(t: int, d:int):
    return t / d if d != 0 else 0

def calculate_idf(D:int, number_document_contain_t):
    res = math.log10(D/number_document_contain_t) if number_document_contain_t != 0 else 0
    return res

def calculate_tfidf(word):
    tfs = {}
    idfs = {}

    # total number do documents
    total_number_of_documents = len(documents) # D


    # number of documents containing term t
    number_of_documents_containing_term_t = 0

    for title, document in documents.items():
        count_terms = defaultdict(int)
        number_time_term_in_document = defaultdict(int) # t
        total_number_of_term_in_document = len(document.split()) # d
       
        for term in document.split():
            count_terms[term] += 1
            number_time_term_in_document[word] = count_terms[word]



        tfs[title] = calculate_tf(number_time_term_in_document[word], total_number_of_term_in_document)
        

    for title, value in tfs.items():
        if value != 0:
            number_of_documents_containing_term_t += 1
    

    for title in documents.keys():
        idfs[title] = calculate_idf(total_number_of_documents, number_of_documents_containing_term_t)


    print(f"\n")
    print(f"TF-IDF for Term {word}")
    print(f"\n")

    print("tfs: ", tfs)
    
    print(f"\n")
    print(f"\n")

    print("idfs: ", idfs)

    tf_idf = {}
    for title in documents.keys():
        tf_idf[title] = tfs[title] * idfs[title]

    print(f"\n")
    print(f"\n")

    print("tf-idf: ", tf_idf)

    
# calculate_tfidf("football")
calculate_tfidf("is")
calculate_tfidf("ball")