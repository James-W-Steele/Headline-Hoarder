LTM=["placeholder"]
SitesFile= open("Sites.txt","r")
Sites=SitesFile.read()
SitesFile.close()
Sites=Sites.split()
HitsFile= open("Hits.txt","r")
Hits=HitsFile.read()
HitsFile.close()
Hits=Hits.split()
SettingsFile=open("Settings.txt","r")
Settings=SettingsFile.read()
SettingsFile.close()
Settings=Settings.split()
LTMenabled=((str(Settings[0]))[4])
LTMenabled=int(LTMenabled)
STMenabled=((str(Settings[1]))[4])
STMenabled=int(STMenabled)
ST=((str(Settings[2]))[10:])
ST=float(ST)
WaitTime=((str(Settings[3]))[9:])
WaitTime=float(WaitTime)
SitePrint=((str(Settings[4]))[10])
SitePrint=int(SitePrint)
import urllib.request
import time
placeholder=1
SmartTime=0
while placeholder==1:
    STM=""
    SitesVisited=0
    SiteData=""
    if SmartTime == 0:
        WaitTime=WaitTime+ST
    if SmartTime == 1 and ST<WaitTime:
        WaitTime=WaitTime-ST
    if SmartTime == 1 and ST>=WaitTime:
        WaitTime=0
    SmartTime=0
    while SitesVisited!=len(Sites):
        CurrentSite=Sites[SitesVisited]
        CurrentSite=str(CurrentSite)
        if SitePrint==1:
            print(CurrentSite)
        SiteData= urllib.request.urlopen(CurrentSite).read()
        SiteData=str(SiteData)
        SiteData=SiteData.replace(">"," ")
        SiteData=SiteData.replace("<"," ")
        SiteData=SiteData.replace("="," ")
        SiteData=SiteData.replace("+"," ")
        SiteData=SiteData.replace("#"," ")
        SiteData=SiteData.replace("%"," ")
        SiteData=SiteData.replace("\\"," ")
        SiteData=SiteData.replace(":"," ")
        SiteData=SiteData.replace("/"," ")
        SiteData=SiteData.replace("'"," ")
        SiteData=SiteData.replace("\""," ")
        SiteData=SiteData.replace(";"," ")
        SiteData=SiteData.replace("{"," ")
        SiteData=SiteData.replace("}"," ")
        SiteData=SiteData.replace("("," ")
        SiteData=SiteData.replace(")"," ")
        SiteData=SiteData.replace("-"," ")
        SiteData=SiteData.replace("."," ")
        SiteData=SiteData.lower()
        SiteData=SiteData.split()
        HitChecked=0
        while HitChecked!=len(SiteData):
            CheckTxt=SiteData[HitChecked]
            individual=0
            while individual!=len(Hits):
                if Hits[individual]==CheckTxt:
                    mode="0"
                    TheHit=(str(SiteData[HitChecked-20]))+" "+(str(SiteData[HitChecked-19]))+" "+(str(SiteData[HitChecked-18]))+" "+(str(SiteData[HitChecked-17]))+" "+(str(SiteData[HitChecked-16]))+" "+(str(SiteData[HitChecked-15]))+" "+(str(SiteData[HitChecked-14]))+" "+(str(SiteData[HitChecked-13]))+" "+(str(SiteData[HitChecked-12]))+" "+(str(SiteData[HitChecked-11]))+" "+(str(SiteData[HitChecked-10]))+" "+(str(SiteData[HitChecked-9]))+" "+(str(SiteData[HitChecked-8]))+" "+(str(SiteData[HitChecked-7]))+" "+(str(SiteData[HitChecked-6]))+" "+(str(SiteData[HitChecked-5]))+" "+(str(SiteData[HitChecked-4]))+" "+(str(SiteData[HitChecked-3]))+" "+(str(SiteData[HitChecked-2]))+" "+(str(SiteData[HitChecked-1]))+" "+(str(SiteData[HitChecked]))+" "+(str(SiteData[HitChecked+1]))+" "+(str(SiteData[HitChecked+2]))+" "+(str(SiteData[HitChecked+3]))+" "+(str(SiteData[HitChecked+4]))+" "+(str(SiteData[HitChecked+5]))+" "+(str(SiteData[HitChecked+6]))+" "+(str(SiteData[HitChecked+7]))+" "+(str(SiteData[HitChecked+8]))+" "+(str(SiteData[HitChecked+9]))+" "+(str(SiteData[HitChecked+10]))+" "+(str(SiteData[HitChecked+11]))+" "+(str(SiteData[HitChecked+12]))
                    if CheckTxt!=STM or STMenabled==0:
                        LTMcount=0
                        MemoryFound=0
                        while LTMcount != len(LTM):
                            Matches=0
                            CurrentMemory=LTM[LTMcount]
                            LTP1=len(TheHit)
                            LTP2=len(CurrentMemory)
                            if LTP1 > LTP2:
                                LTP=LTP2
                            else:
                                LTP=LTP1
                            CP=0
                            while CP!=LTP:
                                if TheHit[CP]==CurrentMemory[CP]:
                                    Matches=Matches+1
                                CP=CP+1
                            if Matches/LTP>=0.9:
                                MemoryFound=1
                            LTMcount=LTMcount+1
                        if MemoryFound==0 or LTMenabled==0:
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",Hits[individual],"has been found on:", Sites[SitesVisited])
                            mode=input("Enter in 1 if you would like the rest of the headline, enter 0 if you would like to resume operation as normal:")
                            STM=CheckTxt
                            SmartTime=1
                            LTM=LTM+([TheHit])
                        if mode=="1":
                            print(TheHit)
                            placeholdertwo=input("Press enter when you're done looking at the headline:")   
                individual=individual+1
            HitChecked=HitChecked+1
        SitesVisited=SitesVisited+1
        time.sleep(WaitTime)