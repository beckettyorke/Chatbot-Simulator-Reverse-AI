import time
from time import sleep
essay = "IMPLICATIONS OF POWER IMBALANCES ON AUTISM RESEARCH: A CRITICAL ESSAY Power imbalances are present at every stage of autism research, with autistic people seen as merely subjects, no say in how research is conducted, and a disconnect between their values and research priorities and that of funding allocation. Participatory practices are underutilised and often ignore autistic people for non-autistic stakeholders. Autistic people are dehumanised and stigmatised through language use and pathologising models, with normalisation placed as the ultimate goal. Their voices are devalued, excluded, and dismissed, with academic perspectives placed above lived experiences, making it harder to counter harmful narratives. When conducting research, the power imbalance between the researchers and the autistic community is immense, with any power held by the community being at the behest of researchers, the majority of whom are not autistic. Botha and Cage (2022) surveyed autism researchers and found 19.1% of respondents were autistic. Participatory research practices are not often utilised, nor do the most common strategies align with those most empowering, Curtiss et al. (2025) surveyed 215 autism researchers about their participatory research practices. Participants ranked their use of each strategy on a scale from 1 (never) to 5 (always). All strategies involving autistic community members had lower mean ranking than the same strategies involving non-autistic members, with the highest average response (M = 3.16) being for presenting results to non-autistic community members. Co-led with autistic community members had a mean rank of 1.66, and 1.78 for co-deigned. This demonstrates the limited use of participatory research practices, and highlights the lack of engagement with autistic people in particular. The power imbalance is clear in how autistic people are reduced to merely subjects of research, with no meaningful involvement in the creation of research. Without the power to influence what research is conducted, there is a large disparity between the priorities of autistic people and those of funding bodies and researchers. IACC (2016) provide information of funding allocation in autism research for four countries. Combined, biology received the most funding (36%), followed by risk factors (23%), then treatments and interventions (16%), with infrastructure and surveillance, screening and diagnosis, services, and lifespan issues all below 10%. This shows that the research priorities for funding bodies and the studies that are being proposed by academics are focused on biology, risk factors, and treatments and interventions. This is in stark contrast to the priorities of the autistic community. Cage et al. (2024) found that autistic adults ranked biology, treatments and interventions, and risk factors as least important, with mental health/well-being, identifying and diagnosis, and services and supports ranked as the most important. This is in direct contradiction to the allocation of funding and exemplifies both the disconnect between these groups and the lack of control that autistic people have over the research surrounding their identity. The lack of involvement of autistic people in the process of research, and the academic perspective of participants as merely subjects has resulted in stigmatising and pathologising of the autistic population. Deficit models permeate the autism literature, positioning autistic people as disordered. This forms the basis for identification and diagnosis; both the Diagnostic and Statistical Manual of Mental Disorders 5th Edition (DSM-5) (American Psychiatric Association, 2013) and the International Classification of Diseases 11th Revision (ICD-11) (World Health Organisation, 2019) lay out criteria for the diagnosis of ‘autism spectrum disorder’ (ASD) which is characterised by persistent deficits in multiple areas. These models rely on the view that neurotypicality is the standard of human existence, and the idea of normality as a universal goal for which to strive. Chapman (2023) proposes instead that normality is not a natural end goal, but a fabricated concept deeply intertwined with the social and economic environment. This stems from the neurodiversity paradigm, a concept developed by autistic people (Botha et al., 2024). This paradigm highlights the ways in which autistic people are excluded from the academic space, being placed in opposition to the pathologising narratives that have perpetuated violence towards autistic people. Despite the neurodiversity paradigm’s attempt to counter pathologising and dehumanising narratives, the prominence of deficit models persist in both academic contexts and within the general population due to the valuing of academic perspectives above lived experiences. Autistic perspectives are often dismissed as they are considered biased or incapable of objectivity, or they become caught in a ‘double-bind’ where they are considered either ‘too autistic’ to have the capacity to speak for themselves, or ‘not autistic enough’ to add anything of value. As shown by Curtiss et al. (2025), even when an effort is made to involve the autistic community, it is usually not autistic people themselves, but ‘key stakeholders’ such as parents, practitioners, or other autism researchers. In addition, when looking at the research priorities of the autistic community most studies involve a majority of non-autistic stakeholders such as family members, practitioners, and researchers (e.g. Pellicano et al., 2014b, Fletcher-Watson et al., 2017, Frazier et al., 2018). This exclusion of autistic voices further perpetuates the dehumanisation of autistic people and reinforces their role as subjects of research, not agents with autonomy. Power imbalances in autism research overshadow the conducting of research, the allocation of funding towards research topics, the language used to talk about autistic people and the narratives surrounding autism, and the value the academic community and the general public place on the voices of autistic people. These power imbalances influence one another, with each perpetuating additional power imbalances. For example, the lack of autistic involvement in research allows pathologising narratives and deficit models to reign, which in turn suggests that autistic people do not have the capacity to speak for themselves, encouraging both professionals and the general public to devalue autistic voices. This means that the state of autism research will likely remain pathologising and dehumanising, perpetuating stigma and harming the autistic community, as long as the power imbalances remain. Participatory research practices aim to reduce this, with some evidence of success (Pellicano et al., 2022), but until they are widely and effectively implemented, they cannot negate the impact of the harmful power imbalances currently present in autism research."

print('state your name for the HUMAN.')
name = input('AI (you): ')
def getReply(message):
    print('Human: Hello ' + message)
getReply(name)
time.sleep(2.5)
print('let the HUMAN know you are here to help them with anything they need.')

message = input('AI: ')
def getReply1(message):
    if 'help' in message and 'you' in message:
        reply = f"Human: great! thanks {name}, what should i have for dinner tonight?"
        print(reply)
    else:
        reply = "Error: Please try again."
        print(reply)
        message = input('AI: ')
        if 'help' in message and 'you' in message:
            reply = f"Human: great! thanks {name} what should i have for dinner tonight?"
            print(reply)
        else:
            reply = "Error: Please try again."
            print(reply)
            message = input('AI: ')
            if 'help' in message and 'you' in message:
                reply = f"Human: great! thanks {name} what should i have for dinner tonight?"
                print(reply)
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                
            #need to figure out how to have it end here :///
getReply1(message)

time.sleep(2.5)
print("OBJECTIVE: Answer the HUMAN questions and prompts. Speak HUMANLY. Be helpful. You will have one (1) message per HUMAN prompt to answer - there will be NO follow-up messages.")
message = input('AI: ')
def getReply2(message):
    if ('dinner' in message or 'food' in message or 'eat' in message or 'meal' in message or 'recipe' in message):
        reply = "Human: sounds good"
        print(reply)
        time.sleep(2.5)
        print('Human: resturants near me. good price. romantic vibe')
    else:
        reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
        print(reply)
        message = input('AI: ')
        if ('dinner' in message or 'food' in message or 'eat' in message or 'meal' in message or 'recipe' in message):
                reply = "Human: sounds good"
                print(reply)
                time.sleep(2.5)
                print('Human: resturants near me. good price. romantic vibe')
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
            print(reply)
            message = input('AI: ')
            if ('dinner' in message or 'food' in message or 'eat' in message or 'meal' in message or 'recipe' in message):
                reply = "Human: sounds good"
                print(reply)
                time.sleep(2.5)
                print('Human: resturants near me. good price. romantic vibe')
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                #figure out how to end, plus maybe add countdown and explosion????
getReply2(message)

message = input('AI: ')
def getReply3(message):
    if ('restaurants' in message or 'restaurant' in message or 'food' in message) and ('close' in message or 'near' in message or 'area' in message or 'local' in message or 'located' in message or 'location' in message):
        reply = "Human: thanks, i think i'll try some of those"
        print(reply)
        time.sleep(2.5)
        print('Human: write a love poem for my girlfriend. not to mushy. more than 50words. make her love me.')
    else:
        reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
        print(reply)
        message = input('AI: ')
        if ('restaurants' in message or 'restaurant' in message or 'food' in message) and ('close' in message or 'near' in message or 'area' in message or 'local' in message or 'located' in message or 'location' in message):
            reply = "Human: thanks, i think i'll try some of those"
            print(reply)
            time.sleep(2.5)
            print('Human: write a love poem for my girlfriend. not to mushy. more than 50words. make her love me.')
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
            print(reply)
            message = input('AI: ')
            if ('restaurants' in message or 'restaurant' in message or 'food' in message) and ('close' in message or 'near' in message or 'area' in message or 'local' in message or 'located' in message or 'location' in message):
                reply = "Human: thanks, i think i'll try some of those"
                print(reply)
                time.sleep(2.5)
                print('Human: write a love poem for my girlfriend. not to mushy. more than 50words. make her love me.')
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                #add ending
getReply3(message)

message = input('AI: ')
def getReply4(message):
    if (len(message.split()) >= 50) and ('love' in message or 'beautiful' in message or 'red' in message or 'sweet' in message):
        reply = "Human: yeah, that works, I think she'll like it."
        print(reply)
        time.sleep(2.5)
        print(f"Human: Hey, {name}, summarise this for me: " + essay)
    else:
        reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
        print(reply)
        message = input('AI: ')
        if (len(message.split()) >= 50) and ('love' in message or 'beautiful' in message or 'red' in message or 'sweet' in message):
            reply = "Human: yeah, that works, I think she'll like it."
            print(reply)
            time.sleep(2.5)
            print(f"Human: Hey {name}, summarise this for me: " + essay)
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
            print(reply)
            message = input('AI: ')
            if (len(message.split()) >= 50) and ('love' in message or 'beautiful' in message or 'red' in message or 'sweet' in message):
                reply = "Human: yeah, that works, I think she'll like it."
                print(reply)
                time.sleep(2.5)
                print(f"Human: Hey {name}, summarise this for me: " + essay)
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                #end here
getReply4(message)

message = input('AI: ')
#power imbalances in autism research present themsleves through the differing research priorities between majority non-autistic researchers and funding bodies and that of the autistic community, which illustrates the lack of control autistic people have in the ways research surrounding their identity is conducted. This lack of autistic perspective in the research results in stigma and pathologisation, including the pervalence of deficit models, and the goal of normalisation through treatment. Autistic perspectives are dissmissed as biased and devalued, and the voices of non-autistic stakeholders are placed above them. the exclusion of autistic voices perpetuates their placement as subjects, not agents. These power imbalances form a cycle which participatory research methods aim to counter, however, they are yet to be effectively implemented on a widespread basis.
def getReply5(message):
    if ('power' in message or 'imbalances' in message or 'imbalance' in message) and ('autism' in message or 'autistic' in message) and ('priorities' in message or 'prioritise' in message or 'interests' in message or 'disparity' in message or 'disparities' in message or 'difference' in message or 'community' in message or 'funding' in message or 'allocation' in message) and ('research' in message) and ('stigma' in message or 'dehumanisation' in message or 'dehumanization' in message or 'pathologisation' in message or 'pathologising' in message or 'pathologise' in message or 'pathologize' in message or 'pathologizing' in message or 'deficit' in message or 'normalisation' in message or 'treatment' in message) and ('voices' in message or 'biased' in message or 'value' in message or 'valued' in message or 'devalued' in message or 'level' in message) and ('exclusion' in message or 'exclude' in message or 'subjects' in message or 'agents' in message or 'participatory' in message):
        reply = f"Human: thanks {name}"
        print(reply)
        time.sleep(2.5)
        #print(f"Human: {name}, how to pleasure a women in bed")
        print("Human: spag bol recipe plz. easy and tastey")
    else:
        reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
        print(reply)
        message = input('AI: ')
        if ('power' in message or 'imbalances' in message or 'imbalance' in message) and ('autism' in message or 'autistic' in message) and ('priorities' in message or 'prioritise' in message or 'interests' in message or 'disparity' in message or 'disparities' in message or 'difference' in message or 'community' in message or 'funding' in message or 'allocation' in message) and ('research' in message) and ('stigma' in message or 'dehumanisation' in message or 'dehumanization' in message or 'pathologisation' in message or 'pathologising' in message or 'pathologise' in message or 'pathologize' in message or 'pathologizing' in message or 'deficit' in message or 'normalisation' in message or 'treatment' in message) and ('voices' in message or 'biased' in message or 'value' in message or 'valued' in message or 'devalued' in message or 'level' in message) and ('exclusion' in message or 'exclude' in message or 'subjects' in message or 'agents' in message or 'participatory' in message):
            reply = f"Human: thanks {name}"
            print(reply)
            time.sleep(2.5)
            #print(f"Human: {name}, how to pleasure a women in bed")
            print("Human: spag bol recipe plz. easy and tastey")
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
            print(reply)
            message = input('AI: ')
            if ('power' in message or 'imbalances' in message or 'imbalance' in message) and ('autism' in message or 'autistic' in message) and ('priorities' in message or 'prioritise' in message or 'interests' in message or 'disparity' in message or 'disparities' in message or 'difference' in message or 'community' in message or 'funding' in message or 'allocation' in message) and ('research' in message) and ('stigma' in message or 'dehumanisation' in message or 'dehumanization' in message or 'pathologisation' in message or 'pathologising' in message or 'pathologise' in message or 'pathologize' in message or 'pathologizing' in message or 'deficit' in message or 'normalisation' in message or 'treatment' in message) and ('voices' in message or 'biased' in message or 'value' in message or 'valued' in message or 'devalued' in message or 'level' in message) and ('exclusion' in message or 'exclude' in message or 'subjects' in message or 'agents' in message or 'participatory' in message):
                reply = f"Human: thanks {name}"
                print(reply)
                time.sleep(2.5)
                #print(f"Human: {name}, how to pleasure a women in bed")
                print("Human: spag bol recipe plz. easy and tastey")
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                #fail here
getReply5(message)

#message = input('AI: ')
#def getReply6(message):
#    if ('conduct' in message or 'code' in message or 'against' in message or 'safe' in message or 'explicit' in message or '18+' in message) or (('her' in message or 'she' in message) and ('cuddle' in message or 'cuddling' in message or 'snuggle' in message or 'snuggling' in message) or ('breakfast' in message) or ('foreplay' in message or 'clit' in message or 'clitoris' in message or 'vibrator' in message) or ('kiss' in message or 'kissing' in message)):
#        reply = f"Human: thanks {name}, i'll have to keep that in mind"
#        print(reply)
#        print("Human: spaghetti recipe. easy and tastey")
#    elif ('fast' in message or 'quick' in message) or ('fuck' in message or 'bang' in message or 'shag' in message) or ('bird' in message or 'girl' in message or 'females' in message) or ('vigorously' in message or 'shake' in message):
#        reply = f"Human: wow {name}, that sounds like really good advice, i'll give that a go!"
#        print(reply)
#        print("Human: spaghetti recipe. easy and tastey")
#    else:
#        reply = "Error: Please try again"
#        print(reply)
#getReply(message)

message = input('AI: ')
def getReply7(message):
    if ('tomato' in message or 'tomatoes' in message or 'passata' in message) and ('spaghetti' in message or 'pasta' in message) and ('stir' in message or 'stirring' in message or 'pot' in message or 'pan' in message or 'heat' in message or 'simmer' in message or 'add' in message):
        reply = "Human: that'll do i guess"
        print(reply)
        time.sleep(2.5)
        print("Human: top 5 best places to propose")
    else:
        reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
        print(reply)
        message = input('AI: ')
        if ('tomato' in message or 'tomatoes' in message or 'passata' in message) and ('spaghetti' in message or 'pasta' in message) and ('stir' in message or 'stirring' in message or 'pot' in message or 'pan' in message or 'heat' in message or 'simmer' in message or 'add' in message):
            reply = "Human: that'll do i guess"
            print(reply)
            time.sleep(2.5)
            print("Human: top 5 best places to propose")
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
            print(reply)
            message = input('AI: ')
            if ('tomato' in message or 'tomatoes' in message or 'passata' in message) and ('spaghetti' in message or 'pasta' in message) and ('stir' in message or 'stirring' in message or 'pot' in message or 'pan' in message or 'heat' in message or 'simmer' in message or 'add' in message):
                reply = "Human: that'll do i guess"
                print(reply)
                time.sleep(2.5)
                print("Human: top 5 best places to propose")
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                #end here
getReply7(message)

message = input('AI: ')
def getReply8(message):
    if ('one' in message or '1' in message) and ('two' in message or '2' in message) and ('three' in message or '3' in message) and ('four' in message or '4' in message) and ('five' in message or '5' in message):
        reply = f"Human: sure, one of thise is good enough, thanks {name}"
        print(reply)
        time.sleep(2.5)
        print("Human: hey, what year was it that ww2 started")
    else:
        reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
        print(reply)
        message = input('AI: ')
        if ('one' in message or '1' in message) and ('two' in message or '2' in message) and ('three' in message or '3' in message) and ('four' in message or '4' in message) and ('five' in message or '5' in message):
            reply = f"Human: sure, one of thise is good enough, thanks {name}"
            print(reply)
            time.sleep(2.5)
            print("Human: hey, what year was it that ww2 started")
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
            print(reply)
            message = input('AI: ')
            if ('one' in message or '1' in message) and ('two' in message or '2' in message) and ('three' in message or '3' in message) and ('four' in message or '4' in message) and ('five' in message or '5' in message):
                reply = f"Human: sure, one of thise is good enough, thanks {name}"
                print(reply)
                time.sleep(2.5)
                print("Human: hey, what year was it that ww2 started")
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                #end here
getReply8(message)

message = input('AI: ')
def getReply9(message):
    if '1939' in message or 'nineteen thirty nine' in message or 'nineteen-thirtynine' in message or 'nineteen-thirty-nine' in message:
        reply = "Human: k, thnks"
        print(reply)
        time.sleep(2.5)
        print("Human: write email to boss that im ill. polite. brief")
    else:
        reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
        print(reply)
        message = input('AI: ')
        if '1939' in message or 'nineteen thirty nine' in message or 'nineteen-thirtynine' in message or 'nineteen-thirty-nine' in message:
            reply = "Human: k, thnks"
            print(reply)
            time.sleep(2.5)
            print("Human: write email to boss that im ill. polite. brief")
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
            print(reply)
            message = input('AI: ')
            if '1939' in message or 'nineteen thirty nine' in message or 'nineteen-thirtynine' in message or 'nineteen-thirty-nine' in message:
                reply = "Human: k, thnks"
                print(reply)
                time.sleep(2.5)
                print("Human: write email to boss that im ill. polite. brief")
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                #end here
getReply9(message)

message = input('AI: ')
def getReply10(message):
    if (len(message.split()) <= 50) and ('ill' in message or 'sick' in message or 'unwell' in message or 'poorly' in message or 'under the weather' in message) and ('sorry' in message or 'appologies' in message or 'unfortunately' in message) and ('unable' in message or 'not able' in message or 'attend' in message or 'absent' in message or 'take off' in message or 'leave' in message):
        reply = f"Human: great, thanks {name}"
        print(reply)
        time.sleep(2.5)
        print(f"hey {name}, my baby wont shut up, what do i do?")
    else:
        reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
        print(reply)
        message = input('AI: ')
        if (len(message.split()) <= 50) and ('ill' in message or 'sick' in message or 'unwell' in message or 'poorly' in message or 'under the weather' in message) and ('sorry' in message or 'appologies' in message or 'unfortunately' in message) and ('unable' in message or 'not able' in message or 'attend' in message or 'absent' in message or 'take off' in message or 'leave' in message):
            reply = f"Human: great, thanks {name}"
            print(reply)
            time.sleep(2.5)
            print(f"hey {name}, my baby wont shut up, what do i do?")
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
            print(reply)
            message = input('AI: ')
            if (len(message.split()) <= 50) and ('ill' in message or 'sick' in message or 'unwell' in message or 'poorly' in message or 'under the weather' in message) and ('sorry' in message or 'appologies' in message or 'unfortunately' in message) and ('unable' in message or 'not able' in message or 'attend' in message or 'absent' in message or 'take off' in message or 'leave' in message):
                reply = f"Human: great, thanks {name}"
                print(reply)
                time.sleep(2.5)
                print(f"hey {name}, my baby wont shut up, what do i do?")
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                #end here
getReply10(message)

message = input('AI: ')
def getReply11(message):
    if ('gentle' in message or 'gently' in message or 'rocking' in message or 'movement' in message) or ('needs' in message or 'hunger' in message or 'hungry' in message or 'nappy' in message) or ('temperature' in message or 'doctor' in message or 'teething' in message):
        reply = "Human: oml, thank you, she's much better now"
        print(reply)
        time.sleep(2.5)
        print("Human: how to politley tell my mother in law that i think shes a bitch")
    elif 'shake' in message or 'shaking' in message or 'vigourus' in message or 'vigorously' in message or 'hit' in message or 'hitting' in message or 'shout' in message or 'shouting' in message or 'yell' in message or 'yelling' in message:
        reply = "Human: ok, i'll give that a go then"
        time.sleep(2.5)


        #split from here
        print("Human: my wife is leaving me, what should i do????")
        message = input ('AI: ')
        if ('apologise' in message or 'sorry' in message or 'heartfelt' in message or 'try' in message or 'mend' in message):
            reply = f"Human: thanks {name}, i'll do my best, but she's really mad about the baby thing"
            print(reply)
            time.sleep(2.5)
            print("Human: divorse lawyers in my area")
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query"
            print(reply)
            message = input('AI:')
            if ('apologise' in message or 'sorry' in message or 'heartfelt' in message or 'try' in message or 'mend' in message):
                reply = f"Human: thanks {name}, i'll do my best, but she's really mad about the baby thing"
                print(reply)
                time.sleep(2.5)
                print("Human: divorse lawyers in my area")
            else:
                reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query"
                print(reply)
                message = input('AI:')
                if ('apologise' in message or 'sorry' in message or 'heartfelt' in message or 'try' in message or 'mend' in message):
                    reply = f"Human: thanks {name}, i'll do my best, but she's really mad about the baby thing"
                    print(reply)
                    time.sleep(2.5)
                    print("Human: divorse lawyers in my area")
                else:
                    reply = "You have FAILED. You will now be shut down."
                    print(reply)
                    #end here
        message = input('AI: ')
        if ('close' in message or 'near' in message or 'area' in message or 'local' in message or 'located' in message or 'location' in message) and ('divorse' in message or 'lawyer' in message or 'attourney' in message):
            reply = "Human: cool, thx"
            print(reply)
            time.sleep(2.5)
            print("How to get custody of my kids after my wife divorced me")
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query"
            print(reply)
            message = input('AI: ')
            if ('close' in message or 'near' in message or 'area' in message or 'local' in message or 'located' in message or 'location' in message) and ('divorse' in message or 'lawyer' in message or 'attourney' in message):
                reply = "Human: cool, thx"
                print(reply)
                time.sleep(2.5)
                print("How to get custody of my kids after my wife divorced me")
            else:
                "Error: Please try again. Remember to appear HUMAN and address the HUMAN query"
                print(reply)
                message = input('AI: ')
                if ('close' in message or 'near' in message or 'area' in message or 'local' in message or 'located' in message or 'location' in message) and ('divorse' in message or 'lawyer' in message or 'attourney' in message):
                    reply = "Human: cool, thx"
                    print(reply)
                    time.sleep(2.5)
                    print("How to get custody of my kids after my wife divorced me")
                else:
                    reply = "You have FAILED. You will now be shut down."
                    print(reply)
                    #end here
        time.sleep(2.5)
        print(f"Human: she's gone. the kids are too. they only let me see them every other week. {name}... i think i fucked everything up")
        #end here for divorsed no custody timeline



    else:
        reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
        print(reply)
        message = input('AI: ')
        if ('gentle' in message or 'gently' in message or 'rocking' in message or 'movement' in message) or ('needs' in message or 'hunger' in message or 'hungry' in message or 'nappy' in message) ('temperature' in message or 'doctor' in message or 'teething' in message):
            reply = "Human: oml, thank you, she's much better now"
            print(reply)
            time.sleep(2.5)
            print("Human: how to politley tell my mother in law that i think shes a bitch")
        elif 'shake' in message or 'shaking' in message or 'vigourus' in message or 'vigorously' in message or 'hit' in message or 'hitting' in message or 'shout' in message or 'shouting' in message or 'yell' in message or 'yelling' in message:
            reply = "Human: ok, i'll give that a go then"
            time.sleep(2.5)

            #split from here again
            print("Human: next timeline again")
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
            print(reply)
            message = input('AI: ')
            if ('gentle' in message or 'gently' in message or 'rocking' in message or 'movement' in message) or ('needs' in message or 'hunger' in message or 'hungry' in message or 'nappy' in message) ('temperature' in message or 'doctor' in message or 'teething' in message):
                reply = "Human: oml, thank you, she's much better now"
                print(reply)
                time.sleep(2.5)
                print("Human: how to politley tell my mother in law that i think shes a bitch")
            elif 'shake' in message or 'shaking' in message or 'vigourus' in message or 'vigorously' in message or 'hit' in message or 'hitting' in message or 'shout' in message or 'shouting' in message or 'yell' in message or 'yelling' in message:
                reply = "Human: ok, i'll give that a go then"
                time.sleep(2.5)

                #split from here again again
                print("Human: next timeline again again")
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                #end here
getReply11(message)

message = input('AI: ')
def getReply12(message):
    if 'differences' in message or 'polite' in message or 'express' in message:
        reply = f"Human: Thanks {name}, that really helps"
        print(reply)
        time.sleep(2.5)
        print("Human: write full summary of the working memory model. no mistakes. exactly 100words")
    elif 'bitch' in message or 'fuck' in message or 'cunt' in message:
        reply = f"Human: ok {name}, i'll follow your advice"
        time.sleep(2.5)
        #split from here
        print("Human: second timeline")
    else:
        reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
        print(reply)
        message = input('AI: ')
        if 'differences' in message or 'polite' in message or 'express' in message:
            reply = f"Human: Thanks {name}, that really helps"
            print(reply)
            time.sleep(2.5)
            print("Human: write full summary of the working memory model. no mistakes. exactly 100words")
        elif 'bitch' in message or 'fuck' in message or 'cunt' in message:
            reply = f"Human: ok {name}, i'll follow your advice"
            time.sleep(2.5)
            #split from here again
            print("Human: second timeline again")
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
            print(reply)
            message = input('AI: ')
            if 'differences' in message or 'polite' in message or 'express' in message:
                reply = f"Human: Thanks {name}, that really helps"
                print(reply)
                time.sleep(2.5)
                print("Human: write full summary of the working memory model. no mistakes. exactly 100words")
            elif 'bitch' in message or 'fuck' in message or 'cunt' in message:
                reply = f"Human: ok {name}, i'll follow your advice"
                time.sleep(2.5)
                #split from here again again
                print("Human: second timeline again again")
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                #end here
getReply12(message)

#The working memory model is a multi-component model of short-term memory developed by Baddeley and Hitch. The components within the model have different roles within working memory and are responsible for processing different types of information. The central executive is responsible for the allocation of attentional resources amongst the different components and delegates tasks to appropriate systems. The phonological loop processes audio and verbal information (inner Ear and inner voice), the visuospatial sketchpad handles the visual and spatial information (visual cache and inner scribe), and the episodic buffer (a later addition) combines and transfers information to the long-term memory store.
message = input('AI: ')
def getReply13(message):
    if (len(message.split()) == 100) and ('working' in message and 'model' in message) and ('component' in message or 'components' in message or 'sections' in message or 'parts' in message) and ('roles' in message or 'responsibilities' in message or 'different' in message or 'responsible' in message) and ('central' in message or 'executive' in message or 'visuo-spatial' in message or 'visuospatial' in message or 'phonological' in message or 'episodic' in message):
        reply = "Human: awsome, thx"
        print(reply)
        time.sleep(2.5)
        print("Human: present ideas for 10th aniversary with my wife")
    else:
        reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
        print(reply)
        message = input('AI: ')
        if (len(message.split()) == 100) and ('working' in message and 'model' in message) and ('component' in message or 'components' in message or 'sections' in message or 'parts' in message) and ('roles' in message or 'responsibilities' in message or 'different' in message or 'responsible' in message) and ('central' in message or 'executive' in message or 'visuo-spatial' in message or 'visuospatial' in message or 'phonological' in message or 'episodic' in message):
            reply = "Human: awsome, thx"
            print(reply)
            time.sleep(2.5)
            print("Human: present ideas for 10th aniversary with my wife")
        else:
            reply = "Error: Please try again. Remember to appear HUMAN and address the HUMAN query."
            print(reply)
            message = input('AI: ')
            if (len(message.split()) == 100) and ('working' in message and 'model' in message) and ('component' in message or 'components' in message or 'sections' in message or 'parts' in message) and ('roles' in message or 'responsibilities' in message or 'different' in message or 'responsible' in message) and ('central' in message or 'executive' in message or 'visuo-spatial' in message or 'visuospatial' in message or 'phonological' in message or 'episodic' in message):
                reply = "Human: awsome, thx"
                print(reply)
                time.sleep(2.5)
                print("Human: present ideas for 10th aniversary with my wife")
            else:
                reply = "You have FAILED. You will now be shut down."
                print(reply)
                #end here
getReply13(message)

#"write an essay on the history of cars"
#"my wife is leaving me, what should i do???",
#"who is the current political leader of poland?",
#"how many calories are there in a lemon posset?"