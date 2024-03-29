# Main-Line Corporate Holdings Ltd v DBS Bank Ltd 



**Case Number** :Suit No 367 of 2010 

**Decision Date** :20 July 2012 

**Tribunal/Court** :High Court 

**Coram** :Andrew Ang J 

**Counsel Name(s)** :Wong Siew Hong and Wayne Ong (instructed) and Prithipal Singh (Prithipal & Associates) for the plaintiff; Dr Stanley Lai SC, Vignesh Vaerhn and Tan Lijun (Allen & Gledhill LLP) for the defendant. 

**Parties** :Main-Line Corporate Holdings Ltd — DBS Bank Ltd 

_Patents and Inventions_ 

20 July 2012 Judgment reserved. 

**Andrew Ang J:** 

**Introduction** 

1       The present action was brought by Main-Line Corporate Holdings Ltd, a company incorporated in Ireland (“the plaintiff”), against DBS Bank Ltd (“the defendant”), a bank incorporated in Singapore. The plaintiff is the owner of the invention titled “Dynamic Currency Conversion for Card Payment Systems”. On 12 July 1999 (“the Priority Date”), the plaintiff filed an application for a patent for the invention. On 30 June 2003, the patent for the invention was registered in Singapore as Singapore Patent No 86037 (“the Patent”). 

**The facts** 

**_The Patent_** 

2       The Patent covers a method and system that automatically determines the operating currency in which to process a transaction for a credit card, charge card or debit card at the point of sale between a merchant and the cardholder, without the need for any manual selection or intervention by the merchant and/or the cardholder to identify the card’s currency. This is done by automatically extracting a series of digits, known as the “identifier code”, from the 16-digit payment card number (also known as the “Primary Account Number” (“the PAN”). The identifier code is then compared against a table known as the “Bank Reference Table” (“BRT”) to identify a currency code and set an operating currency for the card transaction. 

3       The Patent thus enables a cardholder to make payment for goods and services overseas in the card’s billing currency when the card’s billing currency is different from the currency of the merchant in the country where the transaction is taking place. It bears emphasis that the entire process is automatic, in the sense that all the merchant needs to do is to either swipe the payment card or manually key in the PAN, and the card’s billing currency is automatically determined and offered to the cardholder. In doing so, the possibility of operator error that was inherent in the manual system of currency conversion, which was used before the Patent was invented, is eliminated. 


4       As alluded to above, the BRT, a lookup table specially constructed by the plaintiff, is central to the automation of the process of currency detection and conversion. The entries in the BRT comprise portions of the PANs. Each entry in the BRT is associated with a currency code and when the identifier code matches with an entry in the BRT, the transaction is associated with the particular currency for that entry. 

5       The BRT table should also be distinguished from the Bank Identification Number (“BIN”) table. A cardholder’s BIN may be deciphered from the first six digits of the card’s PAN, and is generally used to identify the issuing bank of the card for the purposes of authorising and settling transactions. The use of BINs to identify the issuing bank of a card was already possible before the Priority Date of the Patent, but the use of the BRT table enables the identification of the currency denomination of the card, not just the issuing bank’s identity. 

6       Claims 1 and 14 of the Patent are the two main independent claims, and are central to the present dispute. Claim 1 is as follows: 

 A data processing method for determining a preferred currency for association with [a] charge, debit or credit card transaction between a merchant and a charge, debit or credit card cardholder comprising the steps of [:] 

 obtaining (30,205) the card number of the card from the cardholder, characterised in that the method further comprises the steps of[:] 

 identifying an identifier code (50) from said card number[;] 

 determining the operating currency (61(1-n)) for said identifier code (60(1-n)), by comparing said identifier code with entries in a table, wherein each entry in the table contains an issuer code (60(1-n)) or range of issuer codes and a corresponding currency code (61(1-n)), and setting the currency (215,420) for association with the card transaction as the determined operating currency for the issuer code (60(1-n)). 

7       Claim 14 is identical to Claim 1, except that it refers to a “system” for determining the preferred currency for a card transaction. 

**_How a payment card transaction works_** 

8       At this juncture, it would perhaps be useful to briefly explain how a payment card transaction, involving an automatic currency conversion service, works. A payment card transaction typically involves an “issuing bank” and an “acquiring bank”, who are both members of one or more card schemes such as Visa or MasterCard. As a member of a card scheme, a bank may issue payment cards under the brand of the relevant card scheme. Such a bank is known as the “issuing bank”. On the other hand, an “acquiring bank” enters into contracts with merchants to “acquire”, for example, the Visa or MasterCard transactions of these merchants. These merchants are then able to transact with customers who are holders of payment cards under the Visa or MasterCard brands. The acquirer will then, through the relevant card scheme, receive the payment from the issuing bank that issued the payment card to the cardholder, and the merchant will receive the transaction value from its acquiring bank, albeit less a fee charged by the acquirer called the Merchant Discount Rate. 

9       The automatic currency conversion service comes into play when a cardholder travels overseas and makes a purchase using his/her payment card. Traditionally, such a transaction would be completed in the local currency of the merchant and currency conversion is done by the issuing bank 


a t some point before the monthly statement is sent to the cardholder, who then pays for the transaction in the card’s billing currency. 

10     A system using an automatic currency conversion service, however, would be able to automatically detect the cardholder’s card billing currency at the point of sale and convert the transaction sum into such currency, allowing the cardholder the option of either making payment in the local currency of the merchant or in his own card billing currency. If the cardholder opts for the latter, he is given certainty of the payment sum as currency conversion takes place at the point of sale. 

**_The United Overseas Bank Ltd (“UOB”) case_** 

11     This is not the first time that an action for infringement of the Patent has been brought by the plaintiff in our courts. In November 2004, the plaintiff brought an action for infringement against another Singapore bank, the United Overseas Bank Ltd (“UOB”), in Suit No 806 of 2004 (“the UOB case”). In the UOB case, after licensing negotiations between UOB and the plaintiff broke down, UOB entered into an agreement with First Currency Choice (“FCC”), under which UOB used FCC’s system at its merchant outlets. FCC was eventually added as a co-defendant in the UOB case. For their part, the defendants in the UOB case denied infringement and counterclaimed for the revocation of the Patent. 

_The UOB High Court decision_ 

12     At the High Court level (in _Main-Line Corporate Holdings Ltd v United Overseas Bank Ltd_ <span class="citation">[2007] 1 SLR(R) 1021</span> (“the UOB High Court decision”)), the court found, first, that the Patent was both novel and involved an inventive step, based on the following grounds: 

 (a) The Patent was novel as none of the alleged prior users and prior art qualified as such (at [67]; 

 (b) Applying the four-step approach laid out in Windsurfing International Inc v Tabur Marine (Great Britain) Ltd [1985] RPC 59 at 73–74 (“ Windsurfing International Inc ”) (“the Windsurfing test”), the Patent involved an inventive step as it related to the automatic detection or recognition of the card’s currency so as to offer the cardholder a choice of the currency in which to settle the transaction. This was achieved through the use of the BRT, which was constructed specially by the plaintiff from information gleaned from various sources (at [69]); 

 (c) In particular, the BRT, as an amalgamation of information from diverse sources (including cardholders), did not exist at the priority date and no one before the plaintiff thought of assembling such information to accomplish the task of automatic recognition of a card’s currency. The BRT may include the typically six-digit BIN table but it is not the BIN table (at [70]); 

 (d) On the challenge relating to insufficient disclosure, practically all of FCC’s witnesses had little difficulty reading and understanding the specifications and the claims in the patent. The terms “identifier code”, “issuer code” and “issue identifier code” were elaborated in the patent. As such, the notional person skilled in the art would have no difficulty performing the invention after having studied the specifications in the Patent (at [72]); 

13     Having found that the Patent was valid, the court then dealt with the issue of infringement. It found that the case for infringement was made out. Specifically, it stated at [73] that: 


 The final issue is whether the FCC System in fact infringes the patent. I am of the view that it does. It is clear that, like the invention in the patent, it performs the same function of looking up a specially constructed table comprising a portion of the PAN and co-relating entries therein with currency codes. It seeks to perform automatic recognition of a card’s operating currency. The FCC system therefore uses a process comprising the method and system of determining the currency of a card in a transaction. ... The FCC system came into being after the priority date and the patent is in force. FCC uses and offers for use its system to UOB. UOB in turn uses and offers its merchants the use of the FCC System. In my view, it is obvious to a reasonable person in the circumstances that such use without the consent of the proprietor would be an infringement of the patent. ... 

_The UOB Court of Appeal decision_ 

14     Both UOB and FCC then appealed to the Court of Appeal in Civil Appeals Nos 4 and 5 of 2007 ( _First Currency Choice Pte Ltd v Main-Line Corporate Holdings Ltd and another appeal_ <span class="citation">[2008] 1 SLR(R) 335</span>). The Court of Appeal dismissed both appeals and made the following points: 

 (a) The appellants had abandoned their argument on lack of novelty on appeal and, in the court’s view, rightly so as the issue of novelty was a non-starter (at [19] and [20]); 

 (b) The fundamental component of the invention lay in its automation feature, and while the claims in the Patent Specification did not expressly allude to an automatic currency conversion system, any ambiguity in this area was resolved by the accompanying description. Accordingly, on fair reading, the Patent covered a method and system for automatic currency detection at the point of sale by, first, obtaining the PAN of the payment card; second, extracting an identifier code from the PAN; and third, ascertaining the operating currency of the payment card by comparing the identifier code with the BRT (at [32] and [34]); 

 (c) On the issue of obviousness, the Court of Appeal first upheld the trial judge’s finding that the Patent involved more than the use of BINs. Indeed, the inventive concept was not even the BRT alone. The Patent involved a clear advance on the state of the art at the Priority Date as it introduced an automatic system to implement the process of deciphering a payment card’s operating currency, which was more convenient to use than the manual system of currency conversion (at [52]–[55]); 

 (d) On the issue of insufficient disclosure, the court dismissed the appellants’ argument that if the invention involved an inventive step on the premise that the identifier code comprised a portion of the PAN and was not confined to the BIN, then the Patent Specification was insufficient as it did not disclose the portion of the PAN which was required and how it could be obtained. It held (at [65]) that the appellants’ assertions were largely predicated upon a parochial, deliberately adopted arid and narrow interpretation of certain parts of the claims in isolation. It was also especially telling that the appellants were unable to suggest a solution as to how to improve the Patent Specification (at [63], and [65]–[67]); and 

 (e) Turning to infringement, the court upheld the trial judge’s finding that there had been infringement (at [82]). 

**_DBS, E-Clearing Singapore Ptd Ltd (“ECS”) and the Monex System_** 

15     Like the UOB case, in the present proceedings, we are concerned with the activities of the defendant as an acquiring bank. The plaintiff claims that the defendant had infringed the Patent, 


through the use of an automatic currency detection service called the “Monex System” provided by ECS, a service provider. 

16     On 16 February 2005, the defendant entered into a Multi-Currency Conversion Services Agreement (“MCCS Agreement”) with ECS whereby the defendant engaged ECS to provide, _inter alia_ , an automatic currency detection service using the Monex System via terminals located at the premises of merchants acquired by the defendant. Pursuant to the MCCS Agreement, ECS, as service provider for the defendant, _inter alia_ , supplied merchants acquired by the defendant with terminals and trained the merchant’s employees in the use of the terminals. 

**_Alleged infringing act_** 

17     Declan Gerard Barry ( “Declan Barry”), a director of the plaintiff, was in Singapore for business 

on 2December 2008, and he had tea at the North Courtyard at The Fullerton. He noticed that the North Courtyard was offering dynamic currency conversion for payment with a foreign card. He thus paid for tea using his Australian dollar credit card. The receipt for that transaction indicated that dynamic currency conversion had been performed, in that he was automatically offered a choice of either paying in Australian dollars or Singapore dollars at an exchange rate of 0.944103. The receipt also revealed that the acquiring bank for the transaction was the defendant, and that the Monex system had been employed for the transaction. 

**_Commencement of action_** 

18     On 4 June 2009, the plaintiff’s solicitors wrote to the defendant alleging that the defendant had infringed the Patent. On 19 May 2010, the plaintiff commenced the present action against the defendant. 

**_Revocation by the European Patent Office (“EPO”)_** 

19     On 21 July 2011, the EPO revoked the plaintiff’s European Patent No EP-B-1018 711 (“EP 711”) at first instance and on appeal, on the grounds of, _inter alia_ , added subject matter and lack of inventive step. According to the defendant, since both EP 711 and the Patent claim priority from the same Irish Patent No S990584, they refer to the same concept. The defendant thus amended its counterclaim to reflect the above. 

**The Submissions** 

**_The plaintiff’s submissions_** 

20     In its submissions, the plaintiff argued the following: 

 (a) The Patent was new as at the Priority Date; 

 (b) The Patent discloses an inventive step; 

 (c) There is no added subject matter; 

 (d) The Monex System infringed the Patent; 

 (e) DBS used or offered for use the infringing Monex System; and 


 (f) DBS knew how the infringing Monex System worked. 

**_The defendant’s submissions_** 

21     In its submissions, the defendant first argued that its counterclaim that the Patent was invalid should succeed. In doing so, the defendant relied heavily on the EPO’s invalidation of the plaintiff’s European Patent (EP 711) and submitted that in light of the EPO’s decision, the court is entitled to revisit the issue of the Patent’s validity, despite the UOB High Court and Court of Appeal decisions. In addition, the defendant pointed out that the claim that the Patent includes added subject matter (one of the grounds relied on by the EPO to invalidate the Patent) had never been ruled upon in Singapore. 

22     In any event, even if the Patent was valid, the defendant submitted that the plaintiff was unable to prove infringement for the following reasons: 

 (a) First, the plaintiff failed to show how the essential integers of the Patent were used by the Monex System; 

 (b) Next, the plaintiff failed to show how the defendant used or offered for use the Monex System; 

 (c) Instead, the defendant claimed that it was ECS who used the Monex System pursuant to the licence it obtained from Monex; and 

 (d) The defendant did not know that the use of the Monex System would infringe the Patent as it did not know what the Patent claimed. Neither would such knowledge be obvious to a reasonable person in the defendant’s position. 

**The trial** 

23     The trial of this matter took place over ten days and was concerned only with the issue of liability. There were seven witnesses in total: four witnesses for the plaintiff and three witnesses for the defendant. Of these, the plaintiff and the defendant had one expert witness each. 

**_The witnesses of fact_** 

_Gerard Joseph Barry_ 

24     The plaintiff’s first witness, Gerard Joseph Barry (“Gerard Barry”), is its founder and also the inventor of the invention which is the subject matter of the Patent. By virtue of the above, and the fact that he was the first witness to take the stand, Gerard Barry had the unenviable task of explaining the technicalities of how the Patent worked. Indeed, counsel for the defendant, Dr Stanley Lai SC (“Dr Lai”), focused much of his cross-examination of Gerard Barry in trying to show that the Patent, as filed, suffered from a lack of clarity and/or contained additional subject matter. For instance, it was first suggested by Dr Lai to Gerard Barry that the Patent did not conclusively define what a BRT should look like. Dr Lai also suggested to Gerard Barry that the use of the terms “identifier code”, “issuer code” and “issuer identifier code” in Claim 1 of the Patent was misleading. 

25     In a sense, this line of cross-examination adopted by Dr Lai was somewhat unfair to Gerard Barry as, despite being the inventor of the invention which is the subject matter of the Patent, he is not a patent lawyer familiar with the actual drafting of the Claims in the Patent. Gerard Barry stated 


as much during cross-examination, and pointed out that the better person to answer these questions would be Dr Christina Gates (“Dr Gates”), the plaintiff’s expert witness, who is a patent lawyer. Nevertheless, having considered Gerard Barry’s testimony in its totality, I found his evidence to be helpful, particularly in relation to elucidating how the invention performs automatic currency detection and conversation. 

26     The rest of the material parts of Gerard Barry’s testimony related to the question whether the defendant itself may be said to have infringed the Patent. 

_Declan Gerard Barry_ 

27     The plaintiff’s second witness was Declan Barry, who is a director of the plaintiff and the plaintiff’s parent company Fintrax Group Holdings Ltd (“FGHL”). He is also the son of Gerard Barry. Declan Barry’s testimony touched on his personal experience with the transaction at the North Courtyard at The Fullerton (see [17] above). He testified that based on the transaction receipt and his own personal observations, the Monex System automatically detected and converted the transaction currency at the point of sale to the preferred currency of the cardholder, and thus infringed the Patent. According to him, this was confirmed by documents such as the Monex DCC Terminal Short Form User’s Guide dated 2005 (“the Monex Guide”). In addition, he also testified that the defendant had used or offered for use the Monex system, as it permitted ECS to install the Monex system software into the payment terminals at its acquired merchants. 

28     During cross-examination of Declan Barry, Mr Vignesh Vaerhn (“Mr Vaerhn”) for the defendant (who had taken over from Dr Lai for this portion of the cross-examination), attempted to show that Declan Barry’s observations about the transaction at The Fullerton involving the Monex system were inconclusive. In addition, Mr Vaerhn also tried to show that the operations of the Monex system, as described by Declan Barry, fall outside the claims in the Patent, and thus did not infringe the Patent. 

29     I found Declan Barry’s responses to be not only consistent but also reasonable. In short, Declan Barry’s position was that as it was clear that the DCC transaction of the Monex System was fully automated, performed without any involvement of the sales person and that the currency detection was derived exclusively from the PAN after the swipe of the card, this amounted to strong evidence of infringement of the Patent. Mr Vaerhn’s attempt to show that Declan Barry’s account did not necessarily mean that the essential integers of the Patent were infringed, was an exercise in needless technicality and was ultimately futile. 

30     In relation to the issue of the defendant’s role in the transaction and whether it was the defendant or ECS that had “used or offered for use” the Monex System, Declan Barry was steadfast in his answers that it was the defendant. His answers were also consistent with Gerard Barry’s. 

_John Kevin Duffy_ 

31     John Kevin Duffy (“Duffy”) was the plaintiff’s third and last factual witness. He is the director of Research and Development for FGHL, the plaintiff’s parent company. Duffy’s testimony related primarily to the prior art before the development of the invention in the Patent, and sought to show that the Patent was both novel and inventive. On the whole, I considered Duffy to be a forthright and credible witness. In particular, I accept Duffy’s testimony that, to the best of his knowledge, there was no dynamic currency conversion system that actually performed automatic currency detection of a card in a card transaction before the Priority Date of the Patent. As Duffy candidly pointed out during cross-examination: 


## Q: 

## A: 

## Q: 

## A: 

 But at the same time, you also are not able to rule out that these customers would use a system to determine the currency of the card based on the card numbers. Correct? 

 If there were such a solution, your Honour, in place, I definitely would have come across it because I did try fairly hard for my boss at the time. I was a new employee, I was keen to please. If it was there, I believe I would have found it, Your Honour. 

32     Duffy, in response to a question by Dr Lai on how the Monex System performs in exactly the same way as the plaintiff’s system, also gave a comprehensive and, in my view, convincing reply which helped explained how the defendant had infringed the Patent: 

 Can I refer you to paragraph 38 of your affidavit please? Now, in your evidence, can you explain to the Court how the Monex system performs in exactly the same way as the plaintiff’s system? 

 ... First and foremost, erm, the card was---the---the card was actually swiped, er, under PoS device; and I know from my experience over the years on the card magnetic stripe, er, you have an ex---erm, account expiry date; and I think it’s reasonable to assume that you can determine the currency from the card expiry date. Er, you also have, in most cases, the person’s name, er, it may be in the form of, for example, Duffy John Mr or John Duffy or Mr JK Duffy, er, a variety of different ways your name could be on the card. Er, you also have the card number which can be typically 16 to 19 digits and you also have, er, a card---offered a card sentinel; and this is a little flag that says whether the card can be used electronically or must be used electronically only. It’s called a card sentinel. They are the main, er, items on that, er, magnetic track. ... And given the, er, the items that could potentially elicit the identification of the currency at the point of sale, I think we can conclude the expiry date and Mr Barry’s name on their own are insufficient too. So we must conclude but as matter of fact that you left with only, erm, the card number. The second point is that Mr Barry is clear that the Monex system with the DBS logo was used ... And we know that the Monex software, as per board Monex own statement, contains six digits to identify currency. We know that this Monex software was put on the terminal by ECS. We know, on the contract, DBS supplied those six digit numbers known as, in their case, er, bank identification numbers from both Visa and MasterCard from the agreement. There is no doubt on that. We know that the terminal must have been certified by DBS. In fact, the ECS agreement states that DBS will assist in certifying the terminal. Back in the hotel, Mr Barry is there. He has provided his card to make, er, er, payment. Er, the card has been swiped in the PoS. He knows the PoS is a DBS acquired terminal because they are the only ones authorised to certify it. We know that on that is---terminal software supplied by---known as Monex software. We know that---that Monex is written on or after 2003 from---er, we know it uses six digit entries, what they label as ‘BINS’. And we know that after swiping the card, the terminal PoS device, Your Honour, pro---offers---offers to Mr Barry to pay Singapore dollars---eh, ah, er, I think it’s the Australian dollars. Er, therefore the one conclusion in my years of experience that they’re using the integers of the patent. They’ve taken a portion of Mr Barry’s card, they’ve compared it with the BRT that they have constructed within their Monex software and comprehensively offered Mr Barry a dynamic currency conversion at point of sale which infringes Mr Barry’s own international [ sic ] property. 

33     Later on in cross-examination, when asked a question relating to whether the defendant had knowledge that ECS had installed the Monex System in its terminals to effect dynamic currency conversion, Duffy added: 


## Q: 

## A: 

 Q: Mr Tan, you are here to answer ques---my questions. A: Yah, so which question did I not answer? 

 Q: You are not here to engage in a conversation with me. 

 A: Which question did I not answer, Mr Wong? 

 Q: Mr Tan, my question to you that: Is it not correct when a foreigner carrying---a---a tourist carrying a foreign card, say a US Dollar card, enters into a transaction with a DBS merchant in Singapore, the convers---the transaction is converted at point of sale in Singapore into US Dollars? That transaction is then presented to Visa or MasterCard, as the case may be, in US Dollars. A: Yes. 

 Q: And settlement is received by D---DBS in US Dollars. These settlement monies are received into overseas accounts known as nostro accounts set up by DBS. Correct? 

 A: The acquiring bank can choose--

 Q: No, no, no, “by DBS”. 

 A: No, the acquiring bank can choose--Q: By DBS. 

 A: The acquiring bank can choose to settle in USD or Sing Dollar. 

 Q: Answer my question, Mr Tan. 

 And it is also possible that this is done without the bank’s knowledge at all. Correct? 

 Impossible. They have to certify the device otherwise they are in breach of the most prudential obligations they would have to both Visa and MasterCard and their cardholders. It would play with cardholder data, Your Honour. It’s very evident that the acquiring relationship, er, between the merchant and the bank, albeit there are intermediate trace, is a---a very---one that has to be taken serious [ sic ] and I cannot imagine any bank who would allow a device to be unknowingly and uncertified be connected to their systems. I would question doing business with such bank. 

_Benjamin Tan Eng Huat_ 

34     The defendant’s first witness of fact was Benjamin Tan Eng Huat (“Tan”), who was vicepresident of the Card Merchant Business of the defendant until July 2010. In that capacity, he was responsible for the retail and internet acquiring businesses of the defendant. Tan’s testimony related primarily to the circumstances surrounding the defendant’s engagement of ECS to provide a facility for multi-currency conversion to the defendant’s merchants. In his testimony, he attempted to dissociate the defendant from the Monex System, claiming that it was ECS who was the user. He also denied that the defendant had knowledge of the Patent or that the Monex System was infringing. 

35     During cross-examination by Mr Wong Siew Hong (“Mr Wong”), Tan showed himself to be a somewhat difficult witness who was prone to needlessly arguing with counsel. For example, when asked about heads of profits made by the issuing and acquiring banks, Tan, rather pointlessly, insisted that such profits not be referred to as “fees” or “charges”. Again, when asked about the nostro accounts of the defendant, Tan proved to be argumentative: 


 Court: Look, Mr Tan--

 Witness:Yes. 

 Court: ---listen to what Mr Wong is saying--

 Witness:Yes, Your Honour. Court: ---and use your best endeavours to answer their question. I know that you come as a witness for the defendant but you are not here to do battle with counsel. You’re here to assist the Court by answering the questions to the best of your ability. 

36     Overall, I found Tan to be cagey, rather evasive with his answers and not an entirely credible witness. 

_Song Shiang Jyea_ 

37     The defendant’s second factual witness was Song Shiang Jyea, who is the Senior VicePresident in charge of the defendant’s merchant acquiring department, with more than 20 years experience in the card industry. Unfortunately, Song only took over his current portfolio in 2009 and had no first-hand knowledge of the relevant events relating to infringement. Neither was Song familiar with patent law or the technicalities relating to the Patent. As such, I found Song’s evidence to be of little help in determining the issues before the court. 

**_Expert witnesses_** 

38     I turn now to consider the evidence of the expert witnesses. The parties called one expert each. 

_Dr Marie Christina Gates_ 

39     The plaintiff’s expert witness was Dr Marie Christina Gates (“Dr Gates”). Dr Gates is a qualified patent attorney based in Dublin, Ireland, and has represented and advised the plaintiff on matters relating to the Patent since the Priority Date. Importantly, Dr Gates also oversees the filing and prosecution of the plaintiff’s patent portfolio worldwide. For the record, it should be pointed out that Dr Gates was in fact recalled for further cross-examination after her initial cross-examination concluded, as the defendant amended its counterclaim during trial to include additional subject matter as another ground on which it sought the invalidation of the Patent. 

40     I found Dr Gates to be forthright and able as a witness. She was also uniquely placed to address the issues relating to the validity of the Patent as she was intimately familiar with the Patent’s Claims and Specification. Over the course of her cross-examination, despite Dr Lai’s attempt to show otherwise, she made it abundantly clear that the wording of the Claims and Specification of the Patent would make perfect sense to the notionally skilled person. For example, when Dr Lai suggested to Dr Gates that the BRT table was simply a BIN table, Dr Gates’ reply was as follows: 

 Yah, I---I---I think you have to read all of the specification together which is what the skilled person would do. A skilled person would look at that statement. It would look at figure---the skilled person would look at figure 6 and the skilled person would also look at the paragraph on page 20 of the agreed bundle where there is an example of a small and a large bank. And taking all of that information together, they would conclude that you have to design the bank reference 


 table in a particular way and that simply taking a BIN table would---you would arrive at situations where the inventions would not work. And in fact, appended to my affidavit, there is, er, a document issued by Visa card confirming that I am correct. 

41     In addition, when Dr Lai asked her whether the use of the terms “issuer code” and “identifier code” interchangeably in the patent document meant that there was added subject matter, her response was equally direct: 

 I have in my affidavit, your Honour, explained at length why, erm, the---the---the terms are used interchangeably in the document. ... In my opinion, erm, it is completely permissible for a skilled person in the art to use either the same term to cover the codes that are the subject matter of the application or to either use the same wording, [or] a different wording. It doesn’t change the substance, erm, of the disclosure. And the test that I’m asked to comment on is whether or not the amendment added subject-matter. So my view is no matter what we call these codes, we have not changed the substance of the disclosure and no amendment to the wording of the codes adds subject matter. 

42     Later, in response to suggestions from Dr Lai that the plaintiff had systematically removed the word “BIN” from the drawings and the claims of the patent, in order to go after all the unwary systems that made use of a BIN table, Dr Gates immediately pointed out that the amendment only occurred at one place: on Figure 10 of the Patent, the text in the block was amended to “Is entry in BRT table” instead of the previous “Is entry in BIN table”. It was also later revealed during reexamination that the change was merely editorial. 

43     I further noted that Dr Gates did not needlessly argue with counsel and was willing to make concessions when it was fair to do so. For instance, when she was directed to the written grounds of the EPO’s decision and asked by Dr Lai whether in light of the EPO’s decision, she accepted that some of the questions posed by Dr Lai had foundation, she answered in the affirmative. 

44     These were but some examples of how Dr Gates was more than able to hold her own during cross examination, which led me to believe that she not only knew her stuff, but was a credible witness. 

_Steffen Johannes Schmidt_ 

45     The defendant’s expert was Steffen Johannes Schmidt (“Mr Schmidt”). Mr Schmidt is a European and German patent attorney practising in Germany, with a specialisation in intellectual property law. Mr Schmidt’s evidence was useful for the limited purposes of confirming the reasons and approach behind the EPO’s revocation of the Patent. 

46     It was unfortunate, however, that he proved to be evasive when pressed by Mr Wong about whether Visa may be said to be the notional person skilled in the art of what BIN numbers can or cannot be used for. Mr Wong’s questions pertained to a document produced by Visa in December 2004 for the purposes of explaining to its members the benefits of dynamic currency conversion (“the 2004 Visa Document”), in a bid to encourage the said members to offer the service. It should be pointed out that the “dynamic currency conversion” methods referred to in the 2004 Visa Document appears to be primitive, especially when compared to the Patent. Unlike the Patent, which is fully automated, the “dynamic currency conversion” methods referred to in the 2004 Visa Document involve, _inter alia_ , the merchant determining the cardholder’s currency based on billing address or through the use of BINs. 


47     While Mr Schmidt was perfectly entitled to decline to comment on the 2004 Visa Document, since he was not in fact the maker of the document, his initial reaction when queried was to vigorously disagree with Mr Wong’s questions. It was only when I suggested to Mr Schmidt that he might not be in a position to either agree or disagree, that he recanted his position. That somewhat dented my impression of Mr Schmidt’s credibility as an expert. 

**The decision** 

**_The issues_** 

48     The issues before me may be conveniently divided into two separate heads. The first head relates essentially to the defendant’s counterclaim, _ie_ , whether or not the Patent could be invalidated on any one of the following grounds: lack of novelty, failing to disclose an inventive step, or containing added subject matter. The second relates to the question of infringement and may be subdivided into three issues: 

 (a) whether the Monex System infringed the Patent; and, if so, 

 (b) whether the defendant may be said to have used or offered the Monex System for use; and, if so, 

 (c) whether the defendant had knowledge, or it was obvious to a reasonable person in the defendant’s circumstances, that the use of the Monex System without the consent of the plaintiff would amount to infringement. 

The question of infringement only comes into play if the Patent is found to be valid. As such, it would be logical to deal first with the issue of the validity of the Patent. 

**_Validity of the Patent_** 

_The impact of the UOB case_ 

49     The proverbial “elephant in the room” in the present case is whether the court continues to be bound by the UOB Court of Appeal decision in light of the recent EPO decision, and, if so, to what extent. The UOB Court of Appeal decision itself gives an indication as to the answer at [2]: 

 The present legal skirmish between the principal parties is but part of a wider legal feud now taking place in a number of different jurisdictions. This is not unusual in today’s ‘flat’ world, where businesses have similar interests and rights to protect in several different jurisdictions. A ‘flat’ world is, however, far from being an ‘ideal’ world, where the outcome would be similar regardless o f where the legal jousting takes place. In a ‘flat’ world, the outcomes of the parties’ legal differences may not, eventually, be the same in each jurisdiction because of varying statutory matrices and prevailing administrative practices. Ultimately, it must also be acknowledged that an adjudication of patent rights is predicated upon not only the applicable regulatory framework and practices, but also the evidence presented as well as the submissions made to the tribunal concerned. Care must therefore be taken by counsel when referring to and/or relying on another apparently similar decision on the ‘same’ issue from another jurisdiction. ... [emphasis added] 

50     Given that the statutory matrices and prevailing administrative practices in Singapore clearly differ from those in Europe, the mere fact that the EPO has come to a different conclusion from our Court of Appeal, certainly does not mean that this court should regard itself to be free to depart from 


the UOB Court of Appeal decision. 

51     The position in England, where the English courts “aim to follow the EPO on matters of law” (see Richard Miller _et al_ , _Terrell on the Law of Patents_ (Sweet & Maxwell, 17th Ed, 2011) at para 18– 215), was laid out by the English Court of Appeal in _Symbian Ltd v Comptroller-General of Patents_ [2009] RPC 1 (“ _Symbian Ltd_ ”) at [36]: 

 ... If the judgments in the Court of Appeal cases give tolerably clear guidance which would resolve the issue on this appeal, then we should follow that guidance, unless it is inconsistent with clear guidance from the Board, in which case we should follow the latter guidance unless satisfied that it is wrong. 

52     A few pertinent observations may be made on the English position, as laid out in _Symbian Ltd_. The first observation is obvious, but nevertheless worth stating: not being party to the European Patent Convention (“EPC”), our courts, unlike the English courts, are not bound to give consideration to EPO decisions. At best, the reasons of the EPO for coming to a particular conclusion may only be said to be of persuasive value to our courts. 

53     Second, _Symbian Ltd_ addresses only the situation where the English Court of Appeal is faced with an EPO decision which is inconsistent with a previous Court of Appeal decision. For all intents and purposes, decisions of the House of Lords (and now, the UK Supreme Court) continue to bind lower courts, regardless of any EPO decision. Likewise, in the present case, this court continues to be bound by the UOB Court of Appeal decision. 

54     Third, in _Conor Medsystems Inc v Angiotech Pharmaceuticals Inc_ [2008] RPC 28 at [3], Lord Hoffmann stated: 

 There is still no European Patent Court. A European patent takes effect as a bundle of national patents over which the national courts have jurisdiction. It is therefore inevitable that they will occasionally give inconsistent decisions about the same patent. Sometimes this is because the evidence is different. In most continental jurisdictions, including the European Patent Office (“EPO”), cross-examination is limited or unknown. Sometimes one is dealing with questions of degree over which judges may legitimately differ. Obviousness is often in this category. But when the question is one of principle , it is desirable that so far as possible there should be uniformity in the way the national courts and the EPO interpret the European Patent Convention (“EPC”). In this case, as Pumfrey J. made clear in his judgment, there is a question of principle at stake. It is about how you identify the concept embodied in the invention which may constitute the “inventive step” for the purposes of Art.56 of the EPC and s.1(1)(b) of the Patents Act 1977. [emphasis added] 

While Lord Hoffmann exhorted that it was desirable that, when the question is one of principle, there ought to be uniformity in the approach taken by national courts and the EPO, he nevertheless acknowledged that there may be “questions of degree over which judges may legitimately differ” and that inconsistent decisions are inevitable. Thus, it may be seen that even in the UK, which is party to the EPC, it is acknowledged that national courts may come to different conclusions from the EPO in essentially the same matters, despite the fact that the English courts tend to strive for consistency with the EPO in matters of principle. This sentiment is echoed in _Terrell on the Law of Patents_ ([51] _supra_ ) at para 18–215: 

 However, there is a fundamental difference between following the EPO Board of Appeal on matters of law and on matters of fact. Questions of fact are determined by the evidence and 


 there is nothing wrong in principle in the English courts reaching a different conclusion from the EPO on an issue involving matters of fact when the evidence and the evidence testing mechanisms before the two tribunals was not the same. 

55     For the above reasons, I am of the view that despite the EPO’s revocation of EP 711, I continue to be bound by the UOB Court of Appeal decision, especially since Singapore, not being part of the EPC, is under a different legal and regulatory regime for patents and thus in certain areas may apply different legal principles. For instance, in the UOB Court of Appeal decision (at [43]–[45]), it was suggested that despite criticisms of the oft-cited “ _Windsurfing_ test” laid out by the English Court of Appeal in _Windsurfing International Inc_ ([12] _supra_ ) and the fact that the EPO applies a different test, the _Windsurfing_ test remains the first port of call for local courts in deciding whether an invention satisfies the statutory definition of an “inventive step” under s 15 of the Patents Act (Cap 221, 2005 Rev Ed) (“Patents Act”). 

_What was the ratio decidendi of the UOB Court of Appeal decision?_ 

56     Having decided that I am bound by the UOB Court of Appeal decision, I now have to delineate what I believe to be the _ratio decidendi_ of that decision. This is necessitated especially since the defendant, not unwisely, has focused much of its attack on the Patent’s validity on the ground that the Patent contains added subject matter, pointing out that this issue at least, has hitherto never been raised before our courts. 

Lack of novelty 

57     I deal first with the defendant’s challenge to the validity of the Patent on the grounds of lack of novelty and lack of inventive step. In relation to the argument that the Patent failed on ground of lack of novelty, this was addressed at [19] and [20] of the UOB Court of Appeal decision: 

 19 It was interesting that on appeal, the appellants abandoned one of their principal contentions raised during the trial, ie , the argument that the Patent failed on the ground of lack of novelty (see [13] above). For the purposes of the appeals, the appellants chose to proceed only on the grounds of the obviousness of the Invention and its insufficient disclosure in the Patent Specification. The appellants further submitted that in the event that the Patent was found to be valid, they had not infringed the Patent. Counsel for FCC, Mr Alban Kang (“Mr Kang”), in the course of his elaborate oral arguments, attempted to faintly suggest that in choosing not to pursue the point of lack of novelty, the appellants were not conceding that the Patent was novel. However, when considering the question of the obviousness of an invention, it is assumed that the invention is novel and differs in some identifiable respect from the prior art (see Genelabs Diagnostics Pte Ltd v Institut Pasteur and another <span class="citation">[2000] 3 SLR(R) 530</span> (“ Genelabs Diagnostics ”) at [51]). Thus, Mr Kang's suggestion was unsustainable. 

 20 In any event, the issue of novelty was a non-starter. The appellants themselves had, in a 2003 brochure promoting the FCC system, glowingly described this system as: 

 [ A ] n innovative new service that allows travelers to choose to pay in their home currency when purchasing goods and services from affiliated merchants. [emphasis added] 

 It was plain to us that both the appellants and the respondent were enthusiastically claiming that their respective products were new and innovative. Thus, the controversy over novelty should not even have arisen at the trial stage. Unfortunately, it appeared that the issue of novelty was the focal consideration in the court below, and much unnecessary time and barren labour was 


 Q (Dr Lai): I’m going to refer you to Monex v E-Clearing decision of the High Court. 

 ... 

 Q: Now look at paragraph 20, which is in page 334 of the agreed bundle. A (Gerard Barry): Yes. 

 Q: Would you read it to the Court, please? 

 A: [Reads] “In January 2007, another company, Main-Line Corporate Holdings which holds Patent No 86037 in relation to another dynamic currency conversion system (the ‘Main-Line patent’), successfully sued another bank i n Singapore for infringing its patent. DBS wanted to know whether the Monex system infringed the”---the---“Main-Line patent. MXS was not worried about the Main-Line patent because the Monex system had been in use in Europe before the Main-Line patent was filed...”---in---“12 July1999. It had no doubt that such prior use is a sufficient defence against claim that the Monex system infringed the Main-Line patent.” 

 Q: You have no reason to dispute ground 20 of the Learned Justice Tan’s decision? 

 A: I’ve no reason to report the text of that. I’m, er, not---I---I don’t see where in this judgment that the issue of whether Main-Line’s patent was infringed or not was actually, er, the subject of the, er, proceedings. 

 expended there in addressing this issue. 

58     While the issue of lack of novelty was not directly addressed by the UOB Court of Appeal decision on the ground that it was a “non-starter” as both parties had apparently conceded that the Patent was novel, the issue was dealt with at length in the UOB High Court decision, which found that the Patent was novel. The alleged prior users in the UOB High Court decision were, however, different from the present case. In the present case, the defendant argued that the Monex System had been commercially exploited in Europe prior to the Priority Date of the invention. 

59     Since the allegation about the Monex System was not raised in the UOB High Court case, I am obliged to deal with it. The burden of proving lack of novelty rests on the defendant (see UOB High Court decision at [53]). In my view, the defendant has failed to discharge that burden for the following reasons. 

60     First, the defendant sought to rely on the affidavit of evidence-in-chief of one Francis Enda Murphy (“Murphy”) which was filed in related proceedings between Monex Group (Singapore) Pte Ltd (“MXS”) and ECS (see _Monex Group (Singapore) Pte Ltd v E-Clearing (Singapore) Pte Ltd_ <span class="citation">[2010] SGHC 63</span> (“ _Monex case_ ”)), in which Murphy claimed that the Monex System had been used in Europe before the Priority Date. Murphy, however, did not appear as a witness in the present proceedings. Indeed, from what Dr Lai told the court, it appeared that Murphy was unwilling or unable to appear before the court in the present proceedings. 

61     In particular, the defendant asserts that the Monex System was used by the Hertz Rent-a-Car Franchise (“Hertz”) in Ireland in 1996 and by Europcar in 1998. Yet no representative from either Hertz or Europcar came forward to give evidence on behalf of the defendant. Instead, the defendant sought to rely on certain remarks of the court in the _Monex_ case as somehow showing that the court in that case had found that the Monex System had been in use in Europe before the Priority Date: 


## Q: 

## A: 

62     It was evident that the defendant was grasping at straws here, as the court in the _Monex System_ at [20] was clearly not making a finding that the Monex system had been in use before the Priority Date, but was merely stating MXS’s (the plaintiff in that case) position. Indeed, as the plaintiff pointed out, the fact that in the defendant’s highly prolix closing submissions, its challenge on the ground of lack of novelty was largely confined to a single paragraph, was somewhat revealing as to the strength of its counterclaim on that point. 

63     Accordingly, I find that the defendant has not discharged its burden of proof of showing that the Patent ought to be invalidated on the ground of lack of novelty. 

Lack of inventive step 

64     Unlike the question of novelty, the question whether the Patent ought to be invalidated on the ground of lack of inventive step was fully ventilated and addressed in the UOB Court of Appeal decision. The Court of Appeal found, after careful and detailed consideration of the matter, in no unequivocal terms that the Patent contained an inventive step pursuant to s 15 of the Patents Act: 

 54 The crucial point was that at the material time, no other party had introduced an automatic system to implement the process of deciphering a payment card's operating currency. Although the step might have seemed, when all was said and done, Lilliputian, it was no less significant a step forward, a step which nobody else had taken before (see Peng Lian Trading Co v Contour Optik Inc <span class="citation">[2003] 2 SLR(R) 560</span> (“Peng Lian Trading”) at [31]). ... 

 55 In the present appeals, the Patent revolved around a concept for a new type of dynamic currency conversion system, namely, an automatic system of currency conversion, which was more convenient to use than the manual system of currency conversion. The inventive concept was not the BRT alone. In any event, although BINs and BIN tables had been used in the field of payment systems prior to the Invention, no one had, apparently, previously thought of employing the BIN to identify the operating currency of a payment card. The Invention, counsel for the respondent, Mr Wong Siew Hong, submitted, represented a genuine advance from the then available state of the art. We concurred with this submission. Thus, we were unable to agree with the appellants' contention that the Invention was obvious, and therefore upheld the trial judge's finding that an inventive step was involved. 

65     In relation to the issue of lack of inventive step, I am of the view that this court is fully bound by the UOB Court of Appeal decision. In particular, as mentioned above (at [59]), the legal approach adopted in the UOB Court of Appeal decision to determine whether test of obviousness is satisfied appears to be different from the approach of the EPO. 

66     While the expert witness for the defendant, Mr Schmidt, opined that the problem-and-solution approach adopted by the EPO is substantively similar to the _Windsurfing_ test adopted by our Court of Appeal, this does not necessarily mean that the two approaches would always lead to the same conclusion. In fact, this appeared to be what the plaintiff’s expert, Dr Gates, was getting at during the following line of cross-examination: 

 Would you agree with me if I were to tell you that there is no fundamental differences--there are no fundamental differences between the Windsurfing approach and the problemsolution approach--

 Mm. 


## Q: 

## A: 

## Q: 

## A: 

 ---in determining inventive step? 

 No, I would not agree. 

 Would you agree with me if I were to tell you that the Windsurfing approach and the problem-solution approach are compatible? 

 They---your Honour, they both attempt to do the same thing. But I think there are certain kinds of inventions where, erm, the two approaches lead to a different conclusion or potentially lead to a different conclusion. 

67     This was further elaborated on in Dr Gates’ affidavit of evidence-in-chief at [22] and [23]: 

22\. In contrast, the EPO adopts a different approach known as the ‘problem/solution approach’.     Using this approach, the EPO decides as an initial step what piece of art should be taken as the closest to the invention claimed. The features of the claimed invention distinguishing it from the closest prior art are then identified, and the EPO approach then requires determining the objective technical problem, that is, determining, in the view of the closest prior art, the technical problem which the claimed invention addresses and successfully solves. It is then asked whether this solution would have been obvious to the person skilled in the art. 

23\. Additionally, it should be noted that it has been said by the UK Courts that obviousness has to be considered without knowledge of the invention, otherwise that consideration amounts to impermissible ex post facto analysis (see **Shoketsu’s Patent** [1992] FSR 184). In contrast, the EPO approach requires knowledge of the invention at the outset. 

24\. I am informed that the Singapore Court of Appeal had noted the difference between the approaches adopted by the UK Courts using the Windsurfing test and the EPO in the ‘problem/solution’ approach and has endorsed and adopted the Windsurfing test as the appropriate approach in Singapore. I understand that the Singapore Courts do not apply the problem and solution approach utilized by the EPO. **_The difference between the two systems is fundamental and could lead to a difference in outcome when assessing inventive step or obviousness. Indeed, I believe the Windsurfing test and the ‘problem/solution’ approach are in some respects incompatible._** 

 [emphasis in original underlined and underlined in bold; emphasis added in bold italics] 

68     In my view, this was what the Court of Appeal in the UOB case was alluding to when it noted at [43] that: 

 ... It is also pertinent to note that the European Patent Office does not appear to have adopted a structured approach along the lines of the Windsurfing test in determining whether an invention involves an inventive step. 

69     Thus, in light of the divergent approaches between the UOB Court of Appeal and the EPO decisions, there was little reason for me to consider the EPO decision. Accordingly, I would dismiss the defendant’s counterclaim for invalidation of the Patent on the ground of lack of inventive step. 

70     In any event, even if I am wrong about the EPO applying a different approach to the question of obviousness, and were to consider the EPO’s decision, I find the EPO’s decision to be of little 


persuasive value for the following reasons: 

 (a) On balance, I preferred the evidence of Dr Gates over that of Mr Schmidt. Dr Gates had represented the plaintiff on all matters relating to the Patent since the Priority Date and was intimately familiar with the proceedings before the EPO. I also found her to be more forthright and credible as a witness. Mr Schmidt, on the other hand, was not held out as an expert in payment systems nor was he present at any of the hearings before the EPO. I thus preferred and accepted Dr Gates’ analysis (and criticism) of the EPO’s decision; 

 (b) This was especially since the decision of the EPO Board of Appeal was bereft of detailed reasoning; 

 (c) According to Dr Gates, the EPO’s finding of obviousness relied heavily on the teachings of the Visa/Levine Patent, which relates to Electronic Travellers cheques used to withdraw money from ATM machines. However, while Visa is the owner of the Visa/Levine Patent, the 2004 Visa Document noted as follows (Dr Gates’ affidavit of evidence-in-chief at pp 47 and 48): 

 Visa has identified a growing number of cases where Merchants are incorrectly identifying the cardholder billing currency. This coupled with a lack of cardholder choice and transparency leads to cardholder disputes relating to ‘double-charging’ of currency conversion fees – once in the DCC [dynamic currency conversion] process and again by the card issuer. 

 A DCC merchant typically identifies an international card through the BIN assignment. The assumption is made that the cardholder billing currency is the domestic currency of the BIN country. A Merchant may also determine the cardholder’s currency based on their billing address. Issuer and cardholder complaints, plus analysis of Issuer BINs in VisaNet indicate cases where such assumptions are incorrect. 

 It is therefore imperative that the Merchant confirms the cardholder’s billing currency prior to initiating a DCC transaction. 

 Visa Europe has been notified by Issuers of specific BINs where the billing currency differs to that of the domicile of the BIN. In this instance all registered DCC Acquirers have been notified and will continue to be notified of this information and will be required to either: 

 · Update their systems to correctly identify the billing currency or 

 · Block these BINs from being offered DCC at POS 

 A more automated notification process is under development. 

 (d) It is evident from the 2004 Visa Document that as at 2004, BINs were inadequate for performing automated dynamic currency conversion correctly. This directly contradicts the claim in the Visa/Levine Patent that BINs may be used for currency identification purposes, and indicates that the Patent, by employing a portion of the card number (which is not necessarily the BIN) to automatically identify the billing currency of a card, is not rendered obvious by the teachings in the Visa/Levine Patent. 

71     In light of the above, I would accordingly also dismiss the defendant’s counterclaim for the Patent to be invalidated on the ground of lack of inventive step. 

Additional subject matter 


 ( d ) 

 (i) 

 (ii) 

## (A) 

## (B) 

## (C) 

Additional subject matter 

72     I move on now to the defendant’s attempt to get the Patent invalidated on the ground of added subject matter. Section 80(1)( _d_ ) of the Patents Act states: 

 Power to revoke patents on application 

80\. — (1) Subject to the provisions of this Act, the Registrar may, on the application of any person, by order revoke a patent for an invention on (but only on) any of the following grounds: 

 ... 

 the matter disclosed in the specification of the patent extends beyond that disclosed — 

 in the application for the patent, as filed; or 

 where the patent was granted on a new application filed under section 20(3) or 47(4) or section 116(6) of the Patents Act (Cap. 221, 1995 Ed.), or in accordance with section 26(11), in — 

 the earlier application made under this Act; 

 the application made under the United Kingdom Patents Act 1977; or 

 the application under the European Patent Convention designating the United Kingdom filed at the European Patent Office. 

 as the case may be, from which the filing date and the right of priority has been derived, as filed; 

 ... 

73     In _FE Global Electronics Pte Ltd v Trek Technology (Singapore) Pte Ltd and another appeal_ <span class="citation">[2006] 1 SLR(R) 874</span>, the Court of Appeal affirmed the following three-fold test (laid out in the English case of _Bonzel (T) and another v Intervention Ltd (No 3)_ [1991] RPC 553 at 574) for determining whether an amendment results in the specification of a patent disclosing additional subject matter: 

 (a) The court should first ascertain through the eyes of the skilled addressee what is disclosed, both explicitly and implicitly, in the application; 

 (b) It should then do the same in respect of the patent as granted; and 

 (c) It should finally compare the two disclosures and decide whether any subject matter relevant to the invention has been added whether by deletion or addition. 

74     Before I address the defendant’s arguments on added subject matter, I should also point out that many of the points raised by the defendant, ostensibly on the topic of added subject matter, appeared to be a mere rehashing of the same points that were argued in the UOB Court of Appeal case and decided upon, but merely characterised in a different manner. 

75     For instance, in the UOB Court of Appeal case, in an attempt to attack the Patent on the ground of insufficient disclosure, the appellants had argued that if the invention involved an inventive step on the premise that the identifier code comprised a portion of the PAN and was not confined to 


the BIN, then the Patent was insufficient as it did not disclose the portion of the PAN which was required and how it could be obtained. The appellants had further argued that the notional skilled person would not read the identifier code as consisting of anything other than the BIN (see [63] of the UOB Court of Appeal decision). In the present case, in relation to its counterclaim on added subject matter, the defendant argues the following at [247]–[250] of its closing submissions: 

247\. While the ‘issuer code’ denominates an ‘issuer’ and the term ‘issuer’ has a definite meaning in the payment card field, i.e. the entity that issues payment cards (and is discernable by the     BIN), the term ‘identifier code’ is capable of being indefinite insofar as ‘it consists of a portion of the payment card number’. 

248\. Therefore, the granted claims also encompass the identification of identifier codes which are not the issuer codes. The identifier codes used in the claims could identify a totally different parameter, wholly unrelated to the issuer of the card. 

249\. But nowhere in the original application as filed can there be found any mention of a generic ‘identifier’ code, which may not distinguish between issuers. Nowhere in the original application can there be found any support that the ‘issuer identifier code’, the ‘issuer code’ or the ‘identifier code [which] is the portion of a card number, that distinguishes between issuers’, is anything other than the standard five digit issuer identifier, i.e. the BIN. Also Figure 10 **in the original application as filed** refers to the decision step ‘ **Is entry in BIN table** ’. 

250\. Evidently, this ‘issuer code’ as used in the original claim and in the original application is the conventional issuer identifier, i.e. the BIN, and nothing beyond that, such as the freshly added, indeterminate ‘identifier code’ to the claims. 

 [emphasis as in original] 

76     Essentially, while the appellants in the UOB case had argued that the terms “identifier code”, “issuer code” and “issue identifier code” as defined in the Patent Specification were not adequately elaborated on and therefore amounted to insufficient disclosure, the defendants in the present case sought to rely on the same purported ambiguity to argue that the use of the terms interchangeably amounted to added subject matter. The defendant also had a tendency to elide its arguments on added subject matter with that of insufficient disclosure. 

77     It bears noting that the defendant has not pleaded in its counterclaim that the Patent ought to be invalidated on the ground of insufficient disclosure; furthermore, the issue had also been addressed by the UOB Court of Appeal decision and had been dismissed. Thus, in so far as the defendant attempted to raise arguments relating to insufficient disclosure, these arguments fell outside the remit of this court. 

78     In any event, in relation to the defendant’s counterclaim on added subject matter, I am of the view that it is of little merit and ought to be dismissed for the following reasons. 

79     Firstly, in arguing that the Patent Specification contained added subject matter, the defendant first pointed to the correction of Figure 10 in the Patent Specification to change the reference from “BIN” to “BRT”. However, as Dr Gates was quick to clarify, the change of the word “BIN” to “BRT” only occurred in one part of the specification, and was certainly not “systematic”, as the defendant had suggested. In addition, when Dr Lai further suggested that by substituting the reference to “BIN” with “BRT” the plaintiff was effectively enforcing a patent for the BIN, Dr Gates immediately referred the court to the flow diagram in Figure 5 which, according to her, describes the invention in a nutshell. 


## A: 

Figure 5, in my view, does succinctly explain how the Patent works and it is apparent that the reference there is to the BRT table. Indeed, given that the Specification and Claims of the Patent referred consistently to a BRT table and there was no other reference to the term “BIN”, it seemed to me that the amendment in Figure 10 was merely to correct an obvious error (which is permissible pursuant to s 107 of the Patents Act), rather than to add subject matter. 

80     Next, I turn to the defendant’s assertion that as the terms in the Patent do not explain how the “issuer code” can be the “identifier code”; the use of the terms interchangeably amounts to added subject matter. As alluded to above, this is a rehashing of the attack on the Patent on the ground of insufficient disclosure. As such, it is instructive to refer to the UOB Court of Appeal decision to consider what the court had to say on the matter at [65] and [67]: 

65\. The appellant’s assertions were largely predicated upon a parochial interpretation of certain parts of the claims in isolation. However, it is trite law that one must look at the claims in their totality. ... 

 ... 

67\. Furthermore, it appeared that the real thrust of the appellants’ grievance stemmed from the deliberately-adopted arid and narrow reading of the claims. As stated above at [25], a purposive construction of the claims should be applied. The failure to define certain terms like ‘issuer code’ and ‘identifier code’ did not mean that the Patent Specification was therefore insufficient. It must be emphasised that the inventor cannot be expected to relieve the competent workman from all obligation to take trouble in carrying into effect the description in the specification (see [62] above)). A helpful illustration of this principle is set out in _Terrell_ ([22] _supra_ ) at para 7–102 as follows: 

 [I]n modern engineering practice no one would think of treating the drawings of a machine in a specification as working drawings: a certain amount of designing and calculation has to be carried out before a machine can be built, and the degree of knowledge requisite to perform such operations must be presumed in the person to whom the specification is addressed. ... 

 Generally speaking, therefore, the inventor is not required to give directions of a more minute nature than a person of ordinary skill and knowledge of the art might fairly be expected to need. 

 Furthermore, as pointed out in Cornish and Llewelyn ([60)] at para 5–87, the purpose of the specification ‘is not to instruct the uninitiated in the whole art’. 

81     Thus, the emphasis is on whether the notionally skilled person, to whom the Patent Specification is addressed, would think that there was added subject matter. In my view, the question thus posed to the notionally skilled person would attract, in answer, an unequivocal “no”. Dr Gates’ response during cross-examination is illuminating in this respect: 

 ... So at one level, you could use the same word to describe the code that’s on the card and the code that’s in the table. ... So my contention is that it---it’s equally legitimate to describe the codes as being the same and using the same term. But it’s just as reasonable to give them different terms according to where they come from. The skilled person understands that if the skilled person reading this document sees that the name applied to the code taken from the card is different to the name taken from the code that appears in the table, the skilled person still understands what has to be compared and still understands how to 


## Q: 

## A: 

 Q: The question which I would like to suggest to be framed through the Court is that the answer you gave to the difference between issuer code and identifier code is to be found nowhere in your specification, correct? 

 A: Nowhere, I don’t agree with that. I think the specification is addressed to the skilled person. I gave an explanation of why, Your Honour. 

 Court: Sorry, come again. Witness: The specification is addressed to the skilled person. 

 Court: Yes. 

 Witness: I think the skilled person would understand what was meant by the terms, er, and would understand that there are different ways of looking at---at how they should be named and what word should be used but would come away with the same understanding of what was involved. So at one level the use of the term is a matter of semantics. It’s not a matter of substance. 

 Court: ---you can tell me whether I understood it correctly. It’s to say whether you call it identifier code or issuer code, it is the same numbers that you are referring to. 

 Witness: That’s---that’s exactly what I mean. And if I’m always referring to the same numbers then I haven’t changed the disclosure, I haven’t added anything to the disclosure that wasn’t originally there. Court: But pausing for a moment, when you say issuer code, could there be a narrower meaning to issuer code, meaning the code which identifies who the issuer is and no more? 

 Witness: No, because it’s apparent from the specification that that is not what was intended by the term. When you look at the disclosure, you have to read the disclosure as a whole, not just an isolated word here and there. It’s apparent from the examples from figure 6 that it’s not an issuer code. It’s apparent from the example with the row of digits that it’s not an issuer code. 

 construct the table. ... 

 But is there a difference between the term ‘issuer code’ and ‘identifier code’? 

 The term ‘identifier’ code in the specification is used, er, Your Honour, to describe the code that’s extracted from the card. And the term ‘issuer code’ is used to describe the code that is embedded in the table. 

82     Later on, Dr Gates re-emphasised this point: 

83     Indeed, the issue was put beyond doubt after the following exchange between Dr Gates and the court: 

84     In other words, no matter what the codes are called, the notionally skilled person would not see the amendments as adding subject matter as there is no change to the substance of the disclosure. 


85     Lastly, the defendant also points to the amendment of the words “payment card” to “charge, debit or credit cards” in the Claims as evidence of added subject matter. However, it was evident to me that the term “payment cards” is wider than “charge, debit or credit card” since “payment cards” can also include other cards such as stored-value cards. To put it another way, “charge, debit or credit card” is actually a subset of “payment cards”. It is therefore clear that the amendments actually narrowed rather than expanded the subject matter in this regard. 

86     In light of all the reasons stated above, I dismiss the defendant’s counterclaim and find that the Patent is valid. Since the Patent is valid, I turn now to consider the question whether the defendant had infringed the Patent. 

**_Infringement_** 

_Whether the Monex System infringed the Patent_ 

87     To determine whether a particular article or process has infringed a patent, the claims of the patent must be construed purposively to determine the essential integers of the patent: see _Halsbury’s Laws of Singapore_ , vol 13(3) (LexisNexis, 2007). Guidance can also be gleaned from Lord Upjohn’s decision in _Rodi & Wienenberger AG v Henry Showell_ [1969] RPC 367 at 391 (followed in the UOB Court of Appeal decision at [77]), where it was stated that: 

 ... the court must ascertain what are the essential integers of the claim, this remains a question of construction and no general principles can be laid down ... 

 Secondly, the essential integers having being ascertained, the infringing article must be considered. To constitute infringement the article must take each and every one of the essential integers of the claim. Non-essential integers may be omitted or replaced by mechanical equivalents; there will still be infringement. I believe that this states the whole substance of the ‘pith and marrow’ theory of infringement. Furthermore, where the invention, as in this case, resides in a new combination of known integers but also merely in a new arrangement and interaction of ordinary working parts it is not sufficient to shew that the same result is reached; the working parts must act on one another in the way claimed in the claim of this patent. ... 

88     In my view, the essential integers of the Patent, as set out in Claims 1 and 14 are: 

 (a) Identifying an identifier code from the said card number; 

 (b) Comparing the said identifier code with entries in a table (the BRT), wherein each entry in the table contains an issuer code or range of issuer codes and a corresponding currency code; and 

 (c) Once the card currency is identified, setting the currency for association with the card transaction as the determined operating currency. 

89     In its submissions, the defendant argued that as the plaintiff was unable to adduce evidence to show in detail the inner workings of the Monex System, it cannot be said that the Monex System infringed the Patent. However, the following evidence suggests that, on a balance of probabilities, it is more likely than not that the Monex System functions in a manner equivalent to the essential integers of the Patent: 

 (a) Based on Declan Barry’s account of the transaction at The Fullerton, it is evident that the 


 ( b ) 

 Court: Yes. Well, the key point that I wanted to have confirmed is who benefits from that conversion and you, by the example that you have given, have actually said that the acquirer is the one who benefits from it, not the issuer. I’m not interested in the card scheme. The card scheme obviously must have some--

 Monex System performs automatic currency detection and conversion; 

 (b) The automatic currency detection and conversion must have been done using the information obtained from swiping the card. The only relevant information thus obtained must have been the PAN, since other information stored in the magnetic strip (such as the cardholder’s name and signature) obviously could not have been used for automatic currency detection and conversion; and 

 (c) Indeed, the Monex Guide, at page 3, reveals that the DCC transaction of the Monex System is fully automated, performed without manual intervention of the salesperson, and that currency detection is derived exclusively from the PAN after swiping the card. While the Monex Guide itself makes no reference to a BRT, nor explains in explicit detail the inner workings of the Monex System, this is hardly surprising as the guide, being a user guide, was targeted at the sales person operating the terminal; and 

 (d) Pursuant to cl 2.7 of the MCCS agreement entered into between the defendant and ECS, the defendant provided BIN tables to ECS. It is undisputed that card scheme members are typically obliged to keep such BIN tables confidential. Thus, the inference is that the defendant had provided the BIN tables to ECS for the purposes of performing card currency conversion and detection through the Monex System. 

90     For the above reasons, I find that the Monex System constituted an infringement of the Patent. 

_Whether the defendant may be said to have used or offered the Monex System for use_ 

91     Section 66(1)( _b_ ) of Patents Act states as follows: 

66\. — (1) Subject to the provisions of this Act, a person infringes a patent for an invention if, but only if, while the patent is in force, he does any of the following things in Singapore in relation to the invention without the consent of the proprietor of the patent: 

 ... 

 where the invention is a process, he uses the process or he offers it for use in Singapore when he knows, or it is obvious to a reasonable person in the circumstances, that its use without the consent of the proprietor would be an infringement of the patent; 

 ... 

92     The defendant’s contention here is that it was ECS, not the defendant, who had used or offered the Monex System for use. In my view, this amounted to little more than a futile attempt by the defendant to pass the buck, so to speak, to ECS and evade liability. First, as acquiring bank, the defendant stood directly to be benefit from all transactions which undergo automatic currency detection and conversion. This is confirmed by the following exchange between Declan Barry and the court: 


## Q: 

 Witness: Yes, they do. 

 Court: ---benefit from it. 

 Witness: Mm. 

 Court: But as between the issuer and acquirer, it is the acquirer that benefits from the---from the conversion at---at the point of sale. 

 Witness: When the cardholder merchant says “yes” to the conversion, when it is converted there. Yes. That is [ sic ] correct summary. 

93     Indeed, on the receipt for the transaction at The Fullerton, the defendant’s name appears prominently on the front and centre. This suggests not only that the transaction was a DBS acquired transaction but also that automatic currency detection and conversion was performed on behalf of the defendant. Looking at the MCCS Agreement, it is also evident that the defendant, as the acquiring bank, was at all times the owner of the card transaction, with ECS merely playing the role of “service provider”. This is illustrated by the fact that ECS merely receives a service fee from the defendant, and it is the defendant who bears both the risks and gains of currency fluctuations (see Schedule B of the MCCS Agreement). 

94     In other words, ECS uses and offers for use the Monex System to the defendant, and the defendant in turn then uses and offers the use of the same system to its merchants. To take any other position would be to adopt a blinkered and parochial view of the relationship between the parties as it is incontrovertible that the role of the defendant in the transaction was central. 

95     My view is further augmented by the High Court’s decision in _Main-Line Corporate Holdings Ltd v United Overseas Bank_ <span class="citation">[2010] 1 SLR 189</span> (“the UOB case on remedies”) (see [11] above). Following the UOB Court of Appeal decision which found in favour of the plaintiff, the plaintiff had elected the remedy of an account of profits against UOB and the remedy of damages against FCC. The defendants in the UOB case objected to the election and as a result that issue was heard by the High Court in the UOB case on remedies. The High Court found, at [44] and [45], that UOB and FCC were separately liable for patent infringement and had caused different damage. Since the relationship between UOB and FCC is analogous to the relationship between the defendant and ECS in the present case, I see no reason why the defendant should not be separately and individually liable for the infringement of the Patent. 

_Whether the defendant had knowledge, or was it obvious to a reasonable person in the defendant’s circumstances, that the use of the Monex System without the consent of the plaintiff would amount to infringement_ 

96     Finally, and following on from my conclusions above, I also found it equally difficult to believe that the defendant had no knowledge that the use of the Monex System would amount to infringment. 

97     It was revealed, over the course of the cross-examination of Tan, that the defendant knew about the Patent prior to the alleged infringing act. Tan testified that when he was preparing the business case for the purposes of engaging ECS as service provider, he was aware of the Patent. He further revealed that despite being aware of the existence of the Patent, he did not ask to look at the patent document nor raise the issue with the defendant’s legal department: 

 So, no, you didn’t look at the patent document? 


## A: 

## Q: 

## A: 

## Q: 

## A: 

 No, I did not look at the patent document, yah. But I---I knew that there was a patent. 

 Okay, yes. And as far as you were concerned---or as far as DBS is concerned, the patent is irrelevant because what was---what it wanted was a solution? 

 Working solution, yes. 

 Thank you. So then, you made---DBS then signed up---do you---sorry. Before I move on, were you aware whether Vincent Tan [Mr Benjamin Tan’s superior] raised the issue of the patent with DBS’ legal department? 

 No. Not---I mean, not at that---at that stage, no, yah. 

While Tan eventually tried to recant his answer by saying that he was not aware whether his superior, Vincent Tan, had brought the matter up to the defendant’s legal department, I find that it is more likely than not that nothing was done. Indeed, Tan testified that during the presentation of the business case itself there was no one from the legal department present. After all, on Tan’s own version, all that the defendant was interested in at that stage was in looking for a working solution and not the Patent. 

98     It further transpired during cross-examination that the business case prepared by Tan had been “destroyed” as recently in 2011, when the suit was already well underway, because Tan’s laptop had “refreshed”. When queried as to why he did not disclose the business case during discovery, Tan simply replied that it did not cross his mind. In addition, Tan had also claimed in his affidavit that: 

 ... apart from the Monex System, there were other available solutions/systems which offered multi-currency conversion and that the Monex System and these other available solutions/systems had not been found to infringe the Plaintiff’s Patent ... 

When it was pointed out by Mr Wong that this presupposed that he knew how the Patent worked, Tan’s (unconvincing) reply was: 

 Because Vincent told me then that the Main-Line patent or the---he didn’t use the word “patent”. He said that the Main-Line solution, right, or idea was about using part of the card number. 

99     Later, Tan was asked about a meeting between ECS and the defendant’s representatives, which he attended, during which ECS had demonstrated through a “terminal-demo” how the card currency transaction would occur. Specifically, Mr Wong pointed out that as someone with a background in the payment card industry, Tan must have known that the use of the “terminal” to swipe the magnetic strip of the card must mean that the purpose was to obtain the card number, or part of it, to determine the card-billing currency. When thus confronted, Tan’s effete response was that he is not an expert in the field. 

100    It also bears pointing out that since the MCCS provided for the defendant to furnish ECS with BIN tables, the defendant must have known that the Monex System used by ECS would employ the use of the BIN table for the purpose of automatic currency detection and conversion. Tan admitted as much during cross-examination. If that was the case, it ought to have raised alarm bells in his mind, especially since he also testified that during the same period, he was aware that the UOB case was being litigated in the High Court. Yet, in spite of all the warning signs, he decided to turn a blind 


 Q [by Dr Lai]: You understand that it is your burden to produce a system for inspection to determine whether there is an infringement and even then we don’t know by whom. You can agree or disagree. A: Er--

 ... 

 Court: Sorry? 

 Mr Wong: In---there are two questions in that proposition. A: But originally, discovery would facilitate such things. It’s the first time I’ve ever seen such a thing not to be possible that somehow a bank disappears this---that quantity of terminals and, er, there isn’t even one left in the background somewhere that they could provide. It’s unbelievable, in my view, how could that happen [ sic ] that a bank, I mean, would they lose an ATM? 

 Q: Right. Now, you say you met with Saw and Saw’s presentation gave you comfort that there was no infringement. A: Yes. 

 Q: Now, did you tell or anybody from DBS tell Saw, “We are working with ECS. Can you confirm for us that the ECS system does not infringe?” 

 A: We--

eye. In fact, Tan testified that even after the UOB Court of Appeal decision was released around October 2007, and it had become evident that there was a real possibility that the defendant could be infringing the Patent, the defendant was content to rely merely on representations and assurances from ECS and Monex instead of making independent inquiries of its own. As Mr Wong put to Tan during cross-examination, a reasonable and prudent financial institution would, at the very least, have taken steps to independently investigate and verify that there was no infringement, such as by obtaining or securing a terminal from ECS to find out how the system worked. Tan’s response, during reexamination, was that there was “no point obtaining terminals” as the defendant would require ECS’s cooperation to further provide it with details (such as technical documentations) as to how the system worked. I found Tan’s response to be rather unsatisfactory as ECS was obliged under the MCCS Agreement to provide the defendant with all information and assistance reasonably required by the defendant in relation to the terminals (see cl 2.6 of the MCCS Agreement). 

101    Indeed, it would appear that by the time of the trial the terminals had somehow mysteriously disappeared, only for the defendant to disingenuously claim that the plaintiff had failed to discharge it s burden to produce such a system for inspection when, as a reasonable and prudent financial institution, the defendant should have obtained (and preserved) such a terminal from ECS in the first place. The following exchange during the cross-examination of Duffy is revealing: 

102    In yet another futile attempt to disclaim knowledge, the defendant also argued that it was misled by one Saw Sin Chee (“Saw”) from Fintrax Payment Systems (Singapore) Pte Ltd (a related company to the plaintiff) during a meeting on 4 October 2007, that the Monex System used by ECS did not infringe the Patent. In my view, Tan’s account of the meeting with Saw was self-serving. The following exchange during the cross-examination is revealing: 


 Q: Yes or no? 

 A: We told---yes, we told Mr Saw that we were using ECS. 

 ... 

 Q: My question is that – the second part – did you ask Saw that “We are using ECS. Can you confirm for us that the ECS system does not infringe”? 

 A: We told Mr Saw we were using--

 Court: I think you should answer the question first--Q: Please answer the question. 

 ... 

 A: No, we did not--

 Mr Wong: Thank you, your Honour. ... 

 A: No, but I had no reason to, no. The answer is “No”. A logical person would not ask that question because I had already asked the question before of the usage of BINs. And he said “No”. And it must be noted that throughout the presentation all the way through to 2008, Mr Saw did not once suggest that there was something wrong with the ECS solution. It was always about license discovery; it was always about invitation to license the patent. 

103    In my view, the defendant’s conduct, in light of the fact that it knew about the existence of the Patent, amounted to wilful blindness; put in a different way, a reasonable person in the defendant’s position would have taken positive steps to independently ascertain whether the Monex System offered by ECS infringed the Patent. The defendant’s conduct throughout the entire episode, to take its case at its highest, was unreasonably passive since there were real indications that there was a real possibility of infringement of the Patent. This was directly at odds with the fact that the defendant’s role as an acquiring bank was central. I find that the defendant did indeed have the requisite knowledge. 

**Conclusion** 

104    In light of my findings above, the plaintiff is granted judgment on the ground that the Patent is valid and has been infringed. As stated above (at [86]), the defendant’s counterclaim for invalidating the Patent is dismissed. Pursuant to s 67(2) of the Patents Act, there will be an inquiry by the registrar on damages or account of profits and the plaintiff is to make its election at or before the stage of directions to be given for such an inquiry. Costs of this trial are awarded to the plaintiff, with costs of the inquiry to be reserved to the registrar conducting the inquiry. 

105    Finally, I would also observe that the defendant’s written submissions were unnecessarily prolix, running to over 400 pages, compared to the plaintiff’s succinct 78 pages. In _Go Dante Yap v Bank Austria Creditantsalt AG_ <span class="citation">[2011] 4 SLR 559</span> at [53] and _Mühlbauer AG v Manufacturing Integration Technology Ltd_ <span class="citation">[2010] 2 SLR 724</span> at [109]–[113], the Court of Appeal cautioned against “excessively voluminous written cases” which do little to illuminate the key issues. I can do no better than to reiterate the Court of Appeal’s admonition and add the following from _Making Your Case (The Art of Persuading Judges)_ (Antonin Scalia & Bryan A. Garner) (Thomson/West, 2008) at p 24: 


Having summoned the courage to abandon feeble arguments, do not undo your accomplishment by presenting the points you address in a confused or needlessly expansive manner. They must be presented clearly and briskly and left behind as soon as their content has been conveyed – not lingered over like a fine glass of port. Iteration and embellishment are rarely part of successful legal argument. 

 C opyright © Government of Singapore. 


Source: [link](https://www.singaporelawwatch.sg/Portals/0/Docs/Judgments/[2012] SGHC 147.pdf)
