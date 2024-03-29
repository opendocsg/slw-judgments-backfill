# B2C2 Ltd v Quoine Pte Ltd 



**Case Number** :Suit No 7 of 2017 (Summonses No 4 and 8 of 2018) 

**Decision Date** :20 March 2018 

**Tribunal/Court** :Singapore International Commercial Court 

**Coram** :Simon Thorley IJ 

**Counsel Name(s)** :Danny Ong, Sheila Ng and Rachel Low (Rajah & Tann Singapore LLP) for the plaintiff; Paul Ong and Marrissa Karuna (Allen & Gledhill) for the defendant. 

**Parties** :B2C2 Ltd — Quoine Pte Ltd 

_Civil Procedure_ – _Experts_ – _Appointment of single court expert_ 

_Civil Procedure_ – _Production of documents_ – _Objections_ 

20 March 2018 

**Simon Thorley IJ:** 

**Introduction** 

1       On 27 December 2017, a judgment was handed down in this action dismissing an application by the Plaintiff for summary judgment pursuant to O 14 of the Rules of Court (Cap 322, R 5, 2014 Rev Ed) (“Rules of Court”): see _B2C2 Ltd v Quoine Pte Ltd_ [2017] SGHC(I) 11 (“the Judgment”). The present judgment arose out of consequential disputed applications by the parties: by the Defendant for production of documents under O 110 r 17 of the Rules of Court and by the Plaintiff for the appointment of a single court expert pursuant to O 40. 

2       The underlying facts are set out in paragraphs 1–4, 10 and 15–22 of the Judgment which, for convenience, I repeat below: 

 1 This is an application for summary judgment pursuant to Order 14 of the Rules of Court (Cap 322, R 5, 2014 Rev Ed) (“Rules of Court”) in an action for breach of contract and breach of trust. Following the hearing on 5 December 2017, I indicated that I would not be granting summary judgment and that I would give my reasons for refusing relief in writing. These are my reasons. 

 2 The Defendant is a Singapore registered company which operates a currency exchange platform (the “Platform”) enabling third parties to trade virtual currencies for other virtual currencies or for fiat currencies such as the Singapore or US dollars. The two virtual currencies involved in this action are Bitcoin (“BTC”) and Ethereum (“ETH”). 

 3 The Plaintiff is company registered in England and Wales trading inter alia as an electronic market maker. As an electronic market maker, the Plaintiff provides liquidity on exchange platforms by actively buying or selling at the prices it quotes for virtual currency pairs, thereby generating trading revenue. 

 4 In recent years, there has been a significant growth in virtual currencies of which Bitcoin is perhaps the best known. They are not linked to any particular country, nor regulated by any 


central monetary authority. They are traded for other virtual currencies or traditional currencies on computer networks such as the Platform. 

... 

10     The Platform uses order books to record orders from buyers and sellers for each pair of currencies being traded on the Platform. These are all displayed electronically on what is known as a “Trading Dashboard” which also contains a price chart indicating a current fair market price. It displays real time pricing data both for completed trades on the Platform and for trades on several other major virtual currency exchanges. This is achieved through a software program used by the Platform (the “Quoter Program”). 

... 

15     On 19 April 2017, the Plaintiff sought to buy and sell ETH for BTC. To that end, it placed 12,617 ETH/BTC orders of which only 15 were filled on that date, including seven orders which are the subject of this litigation. The orders were all limit orders. Save for the seven orders, the buy or sell orders were transacted at a price of around 0.04 BTC for 1 ETH. 

16     In particular, at 23:29:35 on 19 April 2017 the Plaintiff sold 46.8384 ETH for BTC at an exchange rate of 0.03969496 BTC for 1 ETH. 

17     According to the Defendant, sometime after 23:30 on that day, a “technical glitch” arose on the Platform. Changes had been made to the passwords and cryptographic keys to some of the Platform’s critical systems. But by an oversight, the Defendant’s operations team did not implement these changes to the login credentials for the ETH/BTC Quoter Program. This apparently caused the ETH/BTC Quoter Program to cease working as it was unable to connect to a database necessary to perform its market price updates. In consequence, all the orders which were on the ETH/BTC order book ceased to be available and no true market price could be set. 

18     For reasons which have not been fully explained in the affidavits, between 23:52:52 and 23:54:33 (just over one and a half minutes), the Plaintiff placed seven orders for the sale of ETH for BTC at an exchange rate of between 9.99999 and 10 BTC for 1 ETH – _ie_ , at a rate approximately 250 times the rate of about 0.04 BTC for 1 ETH previously being quoted. 

19     In normal circumstances, this would no doubt have resulted in the orders not being fulfilled as, being limit orders, it was unlikely that the market would fluctuate so violently that the exchange rate would reach this limit level. 

20     However, there were some market traders (the “Force-closed Customers”) involved in the ETH/BTC market at the time using ETH borrowed from the Defendant. Because the ETH/BTC Quoter Program could not access all the data necessary to establish a true market price, it sought to do so by reference to the only data available to it which were, in effect, only the data arising out of the Plaintiff’s seven orders. These new data caused the Platform to reassess the Force-closed Customers’ leveraged positions and detect that the Force-closed Customers’ collateral had fallen below the maintenance margins. The Platform thus automatically placed Stop Loss orders to sell the Force-closed Customers’ assets at the best available prices to repay the ETH loans. 

21     However, because of the technical glitch, the only available price on the Platform was the price offered by the Plaintiff. Hence, the computer matched the Plaintiff’s seven orders with the 


 BTC held by the Forced-closed Customers. In the event, an aggregate of 3092.517116 BTC was credited to the Plaintiff’s account and 309.2518 ETH debited from that account with corresponding amounts being debited from and credited to the Force-closed Customers’ accounts. 

 22 The following day, the Defendant became aware of the technical glitch and unilaterally reversed the trades, returning the BTC to the Force-closed Customers’ accounts and the ETH to the Plaintiff’s account. 

3       By the Judgment, two issues were held to raise appropriately arguable defences. The first, an argument based upon a document known as “the Risk Disclosure Statement”, is not relevant to the matters currently before me. The second relates to a defence of unilateral mistake at common law which was ruled upon in paragraphs 44–61 of that judgment. Paragraphs 56–57 and 60–61, which address the question of knowledge in relation to unilateral mistake, read as follows: 

 56 So far as actual knowledge of the Plaintiff is concerned, the Defendant’s primary contention is that however the abnormally high limit order price came to be offered, it could not have represented a genuine offer to sell in a realistic market. The Plaintiff must have known that the price was wholly out of line with all the other prices it had been seeking to trade at during that day (all of which were more than 250 times lower). These factors, says the Defendant, are more than sufficient to raise a prima facie case that the “non-mistaken party is probably aware of the error made by the mistaken party” ([ Chwee Kin Keong and others v Digilandmall.com Pte Ltd <span class="citation">[2005] 1 SLR(R) 502</span>] at [41]). 

 57 Indeed, the Defendant goes further and draws attention to the fact that it has sought particulars from the Plaintiff as to how the orders came to be made. However, their request has been refused and the Plaintiff’s evidence in reply does not condescend into any detail as to how the orders came to be made. In paragraph 10.2 of Ms [ sic ] Boonen’s second affidavit dated 19 October 2017, she [ sic ] states: 

 The Orders were placed automatically by the Plaintiff’s proprietary system which seeks to quote prices which are at or near the best available prices on the Platform at a particular point in time. If there were no or few other available orders to sell BTC at that time, then the Plaintiff’s system would naturally quote higher prices to sell BTC. ... 

 This demands an investigation at trial to understand why the system quoted a high price but, more specifically, why it selected 10 BTC for 1 ETH as the exchange rate. 

 ... 

 60 The doctrine of unilateral mistake is well developed in circumstances where the error is a human error and the knowledge or lack of it is directly ascertainable from the humans involved. Where computers are concerned, the law is less well developed. When can the workings of a computer or computer program constitute actual knowledge on the part of the programmer or operator of the computer? In his judgment at first instance in Chwee Kin Keong and others v Digilandmall.com Pte Ltd <span class="citation">[2004] 2 SLR(R) 594</span>, V K Rajah JC (as he then was) made the following observation at [102]: 

 Inevitably mistakes will occur in the course of electronic transmissions. This can result from human interphasing, machine error or a combination of such factors. Examples of such mistakes would include (a) human error (b) programming of software errors and (c) 


 S/N Description of documents 

 1 All documents (including, but not limited to, records, reports, internal communications, external communications, computer screenshots and computer printouts) containing and/or evidencing the automated trading instructions, parameters, criteria, algorithms, strategies and/or source codes that were devised, programmed into and/or utilised by the Plaintiff’s automated and/or algorithmic trading system or software as at 19 April 2017 and which resulted in the Orders being placed and the limit price of each of the Orders being set at 9.99999 BTC or 10 BTC for 1 ETH. 

 transmission problems in the communication systems. Computer glitches can cause transmission failures, garbled information or even change the nature of the information transmitted. This case is a paradigm example of an error on the human side. Such errors can be magnified almost instantaneously and may be harder to detect than if made in a face to face transaction or through physical document exchanges. Who bears the risk of such mistakes? It is axiomatic that normal contractual principles apply but the contractual permutations will obviously be sometimes more complex and spread over a greater magnitude of transactions. The financial consequences could be considerable. The court has to be astute and adopt a pragmatic and judicious stance in resolving such issues. 

 61 In the present case, I do not consider that the Plaintiff’s responses to the Defendant’s arguments are sufficient to deny it the right to a trial. The Defendant’s case on the mistake itself is a cogent one and I accept that a more thorough investigation of the facts behind the setting of the abnormally high offer price is justified in order to place the court in a proper position fully to assess the state of the Plaintiff’s knowledge. Equally, after the full facts are established, it will be possible to examine the law on unilateral mistake where computers are involved in greater detail than was possible on an application for summary judgment. 

4       At a further Case Management Conference (“CMC”) on 11 January 2018, the Defendant indicated that although it had sought certain aspects of disclosure from the Plaintiff in relation to the issue of unilateral mistake, the Plaintiff had declined to comply voluntarily. The Defendant also expressed its intention to issue a summons pursuant to O 110 r 17. This it has now done. In Summons No 4 of 2018 (“the Production Application”), the Defendant seeks: 

 (a) a supplementary list of documents enumerating the documents set out in a Schedule containing 11 different categories (“the Defendant’s Schedule”); and 

 (b) inspection and copying of the listed documents. 

5       For its part, the Plaintiff has now issued Summons No 8 of 2018 (“the Expert Application”) under O 40 r 1 seeking an order for the appointment of a court expert to inquire and report upon certain questions relevant to the workings of the Plaintiff’s automated trading program. 

6       These two summonses were heard by me at a CMC on 20February 2018. For the reasons given orally at the hearing, I declined to order any discovery in relation to categories 5–11 of the Defendant’s Schedule and ordered limited discovery in relation to category 4. Nothing further turns on category 4 for present purposes. 

7       So far as categories 1–3 were concerned, I held that documents falling within these categories were relevant and material to the issue of unilateral mistake. The categories are as follows: 


 2 All documents (including, but not limited to, reports, manuals, handbooks, computer screenshots and computer printouts) which explain and/or evidence (i) the features and specifications of the automated and/or algorithmic trading system or software which was utilised by the Plaintiff to place the Orders; and (ii) any instructions on how the system or software may be used to conduct algorithmic trading. 

 3 All documents (including, but not limited to, records, reports, minutes of meeting, internal communications, external communications, computer screenshots and computer printouts) evidencing the reasons for why the limit price of each of the Orders was set at 9. BTC or 10 BTC for 1 ETH by either the Plaintiff’s human traders or the Plaintiff’s automated and/or algorithmic trading system or software. 

8       As can be seen, these documents all relate to the workings of the Plaintiff’s automated trading system which, for the reasons set out in Mr Maxime Boonen’s fourth affidavit (which was in draft form before me but has since been affirmed), are contended by the Plaintiff to embody highly confidential information. The Defendant requested an adjournment to respond to this draft affidavit which I refused but indicated to Mr Paul Ong, counsel for the Defendant, that if at any time during the hearing he felt that his client’s interests were being prejudiced by the absence of a reply affidavit, he should seek an adjournment. In the event, he did not see the need to do this. 

9       For the purposes of these applications, I assumed and worked on the basis that documents falling within categories 1–3 do indeed contain highly confidential information. It was this factor which lay at the heart of the Plaintiff’s reluctance to allow production of the documents in the normal way and which the Plaintiff contended made an order for the appointment of a single court expert desirable. 

10     At the end of the hearing I informed the parties that I proposed to order: 

 (a) On the Production Application, that the Plaintiff should prepare a supplementary list of documents enumerating the documents in its possession custody or power falling with the description of documents in categories 1–3. This list was to indicate the documents which the Plaintiff contends contain confidential information and that these documents should not be inspected by or on behalf of the Defendant without an order of the Court. 

 (b) On the Expert Application, that an independent court expert should not be appointed and that, in the first instance the Plaintiff should be at liberty to adduce evidence from a single expert in relation to specified issues in the manner set out in more detail below. 

11     I indicated that I would give my reasons for reaching these conclusions in writing. 

**The Production Application: the appropriate approach to confidentiality** 

12     Order 110 r 15 of the Rules of Court provides for a party to serve a request for the production of documents which must describe the documents and state how the documents are relevant and material to the party’s case. This the Defendant has done and I have held that the documents within categories 1–3 are relevant and material. Rule 16 provides that the requested person can object to producing the documents and give the reasons therefore. This the Plaintiff has done, citing confidentiality as the reason for the objection. 


13     Order 110 r 17 provides: 

 17.— (1) The requesting party may, within 14 days after being served a notice of objection, apply to the Court by summons for an order to produce the documents objected to. 

 (2) In an application under paragraph (1), the Court may order the production of the documents objected to if – 

 ( a ) the request to produce was made in accordance with Rule 15(3); and 

 ( b ) none of the following objections apply: 

 (i) lack of sufficient relevance to the case or materiality to its outcome; 

 (ii) legal impediment or privilege; 

 (iii) unreasonable burden to produce the requested document; 

 (iv) loss or destruction of the document that has been shown with reasonable likelihood to have occurred; 

 ( v ) grounds of commercial or technical confidentiality that the Court determines to be compelling; 

 (vi) grounds of special political or institutional sensitivity (including evidence that has been classified as secret by the Government, a foreign government or a public international institution) that the Court determines or the Attorney-General certifies to be compelling; 

 (vii) such considerations of procedural economy, proportionality, fairness or equality of the parties as the Court determines to be compelling. 

 [emphasis added in bold] 

14     Order 110 r 21 provides that O 24 (discovery and inspection of documents) does not apply to proceedings in the Singapore International Commercial Court (“SICC”). 

15     There are material differences in language and approach between the discovery provisions in O 110 and O 24 and, although the Defendant framed its application in the form indicated in [4] above for a supplementary list of documents followed by inspection which would be the norm under O 24, this application fell to be decided under O 110 r 17. In particular, due regard needed to be had to r 17(2)( _b_ )(v) highlighted above. 

16     The difficulties faced by courts when dealing with questions of confidentiality in the course of legal proceedings are well known. There is a public interest in open justice and there is an equivalent public interest in ensuring a fair trial in which both parties have unfettered access to all relevant material. Yet there is a competing public interest in ensuring that confidential information – particularly, trade secrets – of one party does not come into the public domain or become exposed to the possibility of misuse by the other party as a result of legal proceedings. This is particularly so when the parties are competitors. 


17     There are numerous well-known cases in many common law jurisdictions having discovery rules equivalent to those in O 24 which throw light upon the principles involved and the approaches adopted in seeking to balance these competing public interests (see, _eg_ , _Warner-Lambert Co v Glaxo Laboratories Ltd_ [1975] RPC 354 (England and Wales), _Mobil Oil Australia Ltd v Guina Developments Pty Ltd_ [1996] 2 VR 34 (“ _Mobil Oil_ ”) (Australia); _Diagcor Bioscience Incorporated Ltd v Chan Wai Hon Billy_ [2015] HKCU 1853 (“ _Diagcor Bioscience_ ”) (Hong Kong) and _Koger Inc v O’Donnell_ [2009] IEHC 385 (“ _Koger_ ”) (Ireland)). 

18     These were considered by Au-Yeung J in _Diagcor Bioscience_ at [13]–[16]: 

 13 Parties may be competitors in a highly competitive market. Where confidential information or trade secrets are involved, the court has to balance the rights of the parties and the due administration of justice. On the one hand, each party is entitled to discovery of all documents that the other party may place before the court for adjudication. On the other, each party is entitled to be protected against infringements and its confidential information or trade secrets. If the defendant is in fact infringing, it should not be permitted to shelter behind a plea of secrecy. If, however, he is not infringing, he is entitled to have the secrets associated with its process maintained intact. ( Warner-Lambert v Glaxo Laboratories Ltd [1975] RPC 354 at 356, lines 7-14) 

 14 In Roussel Uclaf v Imperial Chemical Industries plc [1990] RPC 45, the English Court of Appeal adopted the principles in Warner-Lambert Co v Glaxo at page 49, lines 36-50: 

 “Each case has to be decided on its own facts and the broad principle must be that the court has the task of deciding how justice can be achieved taking in to account the rights and needs of the parties. The object to be achieved is that the applicant should have as full degree of disclosure as will be consistent with adequate protection of the secret. In so doing, the court will be careful not to expose a party to any unnecessary risk of its trade secrets leaking to or being used by competitors. What is necessary or unnecessary will depend on the nature of the secret, the position of the parties and the extent of the disclosure ordered. However, it would be exceptional to prevent a party from access to information which would play a substantial part in the case as such would mean that the party would be unable to hear a substantial part of the case, would be unable to understand the reasons for the advice given to him, and in some cases, the reasons for the judgment. Thus what disclosure is necessary entails not only practical matters arising in the conduct of the case but also the general position that a party should know the case he has to meet, should hear matters given in evidence and understand the reasons for the judgment.” (page 49, lines 36-50, per Aldous J; page 54, lines 39-40, per Nourse LJ) 

 15 The starting point is that there should be full disclosure of the parties to the litigation of all those materials which are going to be considered and which may be put before the court. The onus is on the party seeking to restrict disclosure to justify it and to show why, in all the circumstances, notwithstanding onerous undertakings as to confidentiality and the like, nevertheless documents should not be shown to the litigant on the other side. Dyson Ltd v Hoover Limited (No.3) [2002] RPC 42, at pp 848-849, §§34-35. 

 16 The Warner-Lambert case , Roussel Uclaf case and Dyson case all involve intellectual property rights. They show that trade secret is no bar to discovery. The court may direct disclosure to selected individuals upon terms aimed at securing that there will not be either use or further disclosure of the information in ways which might prejudice the party making disclosure. 

19     The position was also considered by the Court of Appeal in Victoria in _Mobil Oil_ where Hayne JA 


observed as follows (at 38): 

 Where it is said that the documents are confidential, it may be accepted that the fact that the documents are confidential will not ordinarily be a sufficient reason to deny inspection by the opposite party. In most cases, the fact that the documents may not be used except for the purposes of the litigation concerned will be sufficient protection to the party producing them. But where, as here, the party obtaining discovery is a trade rival of the person whose secrets it is proposed should be revealed by discovery and inspection, other considerations arise. 

 Once the documents are inspected by the principals of the trade rival the information which is revealed is known to the trade rival and cannot be forgotten. Confidentiality is destroyed once and for all (at least so far as the particular trade rival is concerned). To say that the trade rival is bound not to use the documents except for the purposes of the action concerned is, in a case such as this, to impose upon that trade rival an obligation that is impossible of performance by him and impossible of enforcement by the party whose secrets have been revealed. How is the trade rival to forget what internal rate of return the competitor seeks to achieve on a new investment of the kind in question? How is the party whose hurdle rate has been revealed to know whether the rival has used the information in framing a tender? Thus, if the trade rival may inspect the documents concerned, the confidentiality of the information in them is at once destroyed. Is that necessary for the attainment of justice in the particular case? 

20     The relevant authorities were reviewed in detail by Kelly J in the High Court of Ireland in _Koger_. In particular, he drew attention to the decision of Mr Anthony Mann QC sitting as a deputy judge in the High Court of England and Wales in _Sport Universal SA v ProZone Holdings Ltd_ [2003] EWHC 204 (Ch) where disclosure of a particular source code was disclosed to the plaintiffs’ expert and lawyers but not to a representative of the plaintiffs. The Judge concluded: 

 Conclusions 

 The above case law all seems to demonstrate that the restriction which the defendants seek to place on disclosure of the material namely, only to be seen by the experts or alternatively only by experts and the legal advisers but to deny it to even a limited number of persons in the plaintiffs’ organisation is exceptional. Such restriction can be ordered but it is unusual. If such a restriction is to apply, there must be exceptional circumstances which would justify it. 

He ordered a measure of disclosure subject to certain conditions: 

 These conditions will include: 

 (i) An undertaking on oath from the nominated officer of the plaintiffs that the material disclosed will not be used for any purpose other than the conduct of this litigation. 

 (ii) That the documentation will at all times remain within the custody of the plaintiffs’ solicitors who must give an undertaking to the court that they will not part company with such material or allow it to be copied in any way without the defendants consent or leave of the court. They must also undertake on oath that the material will not be used for any purpose other than the conduct of this litigation. 

 (iii) The access to be had by the named officer of the plaintiff to the material will have to be in the presence of the plaintiffs’ solicitors. 


 (iv) That a record be kept of the material examined by that officer and the dates, times and duration of such examination. 

 (v) At the conclusion of the litigation, the material will be returned in its entirety to the defendants’ solicitors. 

21     There is thus no hard and fast rule either requiring disclosure or denying inspection. Each case has been decided on its own facts weighing up the competing public interests referred to in [16] above. Depending upon the degree of confidentiality the approach of the courts has differed, ranging from full disclosure on the one hand to no inspection by anyone whose knowledge of the contents of the documents in question raises a serious risk that the confidentiality in the documents would be jeopardised on the other. 

22     Mr Danny Ong, counsel for the Plaintiff, accepted that this was the approach developed in the common law world in relation to discovery applications made in relation to provisions equivalent to O 24 of the Rules of Court. However he contended that O 110 r 17 establishes a different regime that has its origin in the rules and practice of arbitration tribunals rather than the rules of court referred to in the authorities cited above, so different principles apply. 

23     The wording of the exception in O 110 r 17(2)( _b_ )(v) has its origin in Art 9(2)( _e_ ) of the International Bar Association Rules on the Taking of Evidence in International Arbitration (“the IBA Rules”). Mr Danny Ong referred me to some commentaries on those Rules and submitted that if the Court determines that the confidentiality objections are compelling, the Defendant has no basis to ask the Plaintiff to produce the confidential document to any extent, including under a controlled disclosure regime. 

24     He relied particularly on passages in Reto Marghitola, _Documentary Production in International Arbitration_ (Kluwer Law International, 2015) at pp 90–91: 

 §5.11 COMMERCIAL OR TECHNICAL CONFIDENTIALITY 

 [A] Introduction 

 The issue of commercial and technical confidentiality is underestimated by a considerable part of the arbitration literature which tends to focus more on the legal professional and settlement privileges as well as on the confidentiality of arbitral proceedings. However, commercial and technical confidentiality is an important reason to limit document production in practice. 

 This objection must be seen against its economic background. Companies can protect their knowhow through two different methods: either by registering a patent or by keeping the know-how secret. The first method has the disadvantage that the know-how becomes public, but the benefit of exclusivity for a limited period of time. In the opinion of the German Federal Court of Justice, a trade secret is often more valuable than an intellectual property right. 

 This issue is particularly salient when the parties in dispute are competitors and the facts of the case occurred recently. In such situations, the fear that the opposing party gains a competitive advantage by learning trade secrets can be a dominant factor in the party’s considerations on document production. 

 ... 


 [C] Complete Exclusion of Evidence Is the Exception 

 The IBA Rules provide two rules that limit document production due to technical or commercial confidentiality. Pursuant to Article 9(2)( e ) IBA Rules, technical and commercial confidentiality is a reason to exclude document production if the confidentiality concerns are ‘compelling’. In addition, Article 9(4) IBA Rules provides the possibility of ‘suitable confidentiality protection’ when evidence is presented. 

 Neither the IBA Rules nor the Commentary to the IBA Rules defines technical and commercial confidentiality. Moreover, the word “compelling” is not defined... 

25     Mr Danny Ong accepted that under Article 9(4) of the IBA Rules, it is possible for an arbitrator to permit disclosure on specific terms such as redaction of confidential information, production of documents for counsel and experts only or the use of a confidentiality expert. However, he said that once it is determined that the evidence as to confidentiality was compelling, the arbitrator (and by extension, this Court) has no option but to refuse production. 

26     The problem with this contention is that the word “compelling” is, as Marghitola accepts, not defined. The word immediately poses the question, “How compelling?” 

27     In para 11.7.8 of Jeffrey Waincymer’s _Procedure and Evidence in International Arbitration_ (Kluwer Law International, 2012), the author states: 

 ... Another important consideration is to determine what is meant by the requirements that it be ‘compelling’. At the very least, this suggests a presumption in favour of disclosure, absent strong reasons to the contrary. ... 

28     In Nathan D O’Malley’s _Rules of Evidence in International Arbitration: An Annotated Guide_ (Informa, 2012), at para 9.88, it is stated: 

 ... As noted above, the IBA Rules maintain the general principles in article 3.13 that all documents are to be kept confidential and used only for the purposes of the arbitration. In addition to this broad rule on confidentiality, a tribunal may also issue a specific procedural order setting rules for the protection of confidentiality that are binding on the parties or instructions to redact sensitive portions of the requested documentary evidence. 

29     Neither of these authors seeks to identify how the line should be drawn as a matter of generality and I doubt it can be done. Each case must turn on its own facts. To my mind, crucial to determining where the line should be drawn in each case is a balancing of the degree of prejudice to one party of risking disclosure of its confidential information and the degree of prejudice to the other of being denied access to documents which are relevant and material to the resolution of the dispute in question. 

30     Whilst therefore I accept Mr Danny Ong’s submission that the IBA Rules do permit arbitrators to exclude inspection where the evidence of confidentiality is sufficiently compelling, I do not accept that this is a binary question such that “sufficiently compelling” means no inspection and “insufficiently compelling” means full inspection. The IBA Rules expressly permit a middle course of limited inspection with a presumption in favour of permitting a degree of inspection. 

31     Turning to O 110 r 17(2)( _b_ )(v), which has been set out above at [13], it is plain that once the Court concludes that the grounds of commercial or technical confidentiality are compelling, it has no 


power to order production. But again there is no definition of “compelling”. Neither is there the equivalent of Article 9(4) of the IBA Rules expressly permitting protection measures short of refusing any form of inspection. 

32     The discovery process under O 110 is intended to institute a simplified process compared to O 

24\. Disclosure is only required of documents that are relevant and material and there is no general discovery. Undoubtedly, the Court can, in an appropriate case, pursuant to O 110 r 17(2)( _b_ )(v), refuse production where there are suitably compelling grounds. But “compelling” does not, in my judgment, require regard to be had only to the concerns and needs of the party whose confidential information is relevant and material. “Compelling grounds” means grounds which lead the Court to the conclusion that in the circumstances of the case there is no solution which commends itself to the Court other than refusal. 

33     The circumstances of the case will always require some weight to be attached to the interests of a fair trial. Hence the importance of considering the possibility of limiting access to the documents, redactions and provisions of the nature imposed in _Koger_ (see [20] above). 

34     Accordingly, in my judgment, whilst O 110 r 17(2)( _b_ )(v) empowers the Court to refuse disclosure in such a case, it does not fetter the power of the Court in other cases to take such measures short of refusing disclosure as are calculated on the facts of the case to ensure the best balance between the interest of confidentiality on the one hand and the interest of a fair trial on the other. 

35     I thus cannot accept Mr Danny Ong’s submission set out in [22] above that the effect of O 110 r 17 mandates a different approach to dealing with discovery of confidential documents to that which exists under O 24. To my mind, the guidance obtained from the authorities under discovery provisions in the other common law jurisdictions referred to above are equally applicable to proceedings before the SICC. 

**A single court expert?** 

36     By O 110 r 3, the order relating to the appointment of a court expert, O 40, applies to actions in the SICC. Order 40 allows the Court to appoint an expert, preferably a person agreed by the parties, to inquire into and report upon questions of fact or opinion (not involving questions of law or of construction). 

37     Order 40 r 2(1) provides: 

 The court expert must send his report to the Court ... and the Registrar must send copies of the report to the parties or their solicitors. 

Rule 4 permits any party thereafter to apply to the Court for leave to cross-examine the expert on his report and r 6 specifies that on giving reasonable notice, any party may call one expert witness to give evidence on the question reported by the court expert. 

38     The object of O 40 is to enable parties to save costs and the expense of engaging separate experts in respect of a technical question which can be resolved quickly ( _Singapore Civil Procedure 2018_ vol 1 (Foo Chee Hock gen ed) (Sweet & Maxwell, 2018) at para 40/1/2). At para 40/6/1, it is stated that the appointment of a court expert depends upon whether it would lead to a just, expeditious and economical disposal of an action. 


39     The Plaintiff contended that, on the facts of this case, the appointment of a court expert would save both time and costs and serve to address the Plaintiff’s confidentiality concerns. It accepted that the nominated court expert would have to be provided with all relevant documents and that categories 1–3 of the Defendant’s application for discovery did define such documents. The Plaintiff was willing to disclose those documents and any other documents which the expert requests to such an expert, subject to a confidentiality undertaking and other protective measures. 

40     Both parties provided a schedule setting out the issues which it considered the experts (whether appointed by the Court or by the parties) should address. At the end of the hearing I ruled out certain questions which involved the experts giving opinion evidence on market practice and market manipulation. I directed the parties to seek to agree on the wording on certain factual issues which in simple terms would serve to answer the question as to how the Plaintiff’s trading system came to place the limit orders the subject of this action at the unusual exchange rate, some 250 times the previous market rate. 

41     The Plaintiff contended that the fact that these were purely factual questions further supported its request for a court expert. Mr Danny Ong drew my attention to the case of _Abbey National Mortgages PLC v Key Surveyors Nationwide Ltd_ [1996] 1 WLR 1534 and the observations of Jacob LJ in _Dyson Ltd v Qualtex (UK) Ltd_ [2006] EWCA Civ 166 to support his assertion that the Courts should be more willing to order a single court expert where purely factual questions arise. I am far from sure that these authorities lay down such a proposition but, as a matter of principle, he might be right. While the opinions of reasonable men can differ, the evidence of an expert on an issue of fact within his field of expertise is less likely to be controversial. This is particularly so when both parties are themselves working in the field and will therefore themselves have inhouse expertise which will enable the validity of the court expert’s report readily to be assessed. 

42     But therein lies the problem where confidential information is involved. If a court expert is instructed to report on an issue which requires him or her to have access to confidential information, how is the opposing party to assess the validity of the report without having access to that material? 

43     The Plaintiff proposed a detailed order relating to the appointment of and reporting by the court expert. This required time for the parties to agree upon the expert or, in default, for him or her to be appointed by the Court. It required time for the expert to provide the necessary undertakings as to confidentiality, for him or her to be provided with the documents and to ask for such further documents as might be required and thereafter further time to produce the report. 

44     It was proposed that the report be adduced in evidence in a confidential manner. There were no provisions which addressed the possibility of cross-examination of the expert under O 40 r 4 or for the giving of expert evidence on behalf of the parties under r 6. 

45     Mr Paul Ong highlighted the fact that, where one party has no knowledge of the material underlying the report of a single court expert, it is unreasonable to expect it to accept that report at face value unless, of course, it is wholly favourable to that party’s case. He contended that in these circumstances it would be unlikely to save time and costs to appoint a single court expert. On the facts of this case, he felt that whatever the report said, it was likely that the Defendant would wish to have the opportunity, in some way, to satisfy itself that the report was full and fair. He accepted that if the Court was satisfied that the report relied upon confidential information, it might be proper to provide for restricted inspection by an independent expert on terms such as those imported in _Koger_. 

46     I consider that there is, on the facts of this case, substance in those submissions. At present, 


we do not know what information the notional report of the single court expert will rely upon, to what extent the Plaintiff will contend that that information (taken by itself) constitutes confidential information or how compelling will be its reasons for either refusing inspection at all or for imposing stringent conditions on inspection. We do not know whether the Defendant will seek to cross-examine the expert or whether it will seek to adduce evidence from its own expert. 

47     These are matters which can best be considered once an initial report has been prepared. To my mind, the balance has to be drawn between ordering a single court expert to report and requiring the Plaintiff to instruct an independent expert to produce a report on behalf of the Plaintiff. In my judgment, it will be far quicker and cheaper for the Plaintiff to instruct an independent expert. Time will be saved in identifying the expert and the Plaintiff’s in-house experts can assist the independent expert in getting up to speed on the precise technology involved. They can also answer the expert’s questions and provide any further documents rapidly. A single court expert will thus not be appointed. 

**The appropriate way forward** 

48     The Plaintiff’s independent expert will have to have access to all relevant and material documents which the Plaintiff accepts are those described in categories 1–3. It is therefore appropriate that those documents should be identified and listed in a list of documents. In that list, the Plaintiff should highlight all documents for which a claim to confidentiality is made. The list of documents (but not the documents themselves) should be filed at court and served on the Defendant. 

49     The Plaintiff’s independent expert should be supplied with the documents on the list (and any other documents requested by him which should be the subject of a supplemental list) and then prepare a report dealing with the specified issues of fact. Once the report is prepared, the Plaintiff should identify which parts of the report and which documents referred to are said to be confidential. A redacted version of the report should also be prepared in which parts containing information which the Plaintiff contends is confidential are obscured. 

50     The redacted version shall be filed at court and served on the Defendant and shall be free for inspection in the normal way. In addition, one copy of the unredacted report and supporting documents shall be filed at court (and be the subject of a protective order) and one copy supplied to the Defendant’s solicitors. These copies may, if the Plaintiff wishes, be numbered copies. 

51     Prior to supply to the Defendant’s solicitors, the solicitors instructed in this action must each give an undertaking that the unredacted parts of the report and any documents said to be confidential will at all times remain within their custody and will not be inspected otherwise than by them, that they will not part company with such material or allow it to be photocopied, scanned or otherwise reproduced in any other way and that they will not disclose the contents of the material or discuss them with the Defendant or any third party, without the Plaintiff’s consent or leave of the court. They must also undertake that the material will not be used for any purpose other than the conduct of this action. 

52     In the meantime, the Defendant should identify the independent expert it would propose to consult and name one officer in the company capable of understanding the report when explained to him or her but whose future career will not be undermined by being possessed of any confidential information which (s)he receives subject, in both cases, to an appropriate personal confidentiality undertaking. This should be done at an early stage so that any challenges by the Plaintiff to the suitability or integrity of either person can be reduced to writing and ruled upon, if necessary. In requiring this, I should make it clear that at this stage I am not deciding whether or not the provisions 


of O 110 r 17(2)( _b_ )(v) will serve to prevent disclosure of the report or part of it to either person. 

53     Time limits for carrying out these steps should be proposed by the parties for approval by the Court or, in the event of disagreement, will be ordered by the Court. 

54     A further CMC should then be held to decide whether the Defendant needs to instruct an expert, what material (if any) that expert should have access to and on what terms and to consider whether, at that stage, any officer of the Defendant should have access to any and, if so, what material or information and on what terms. I appreciate that this will necessitate the Defendant’s advisors initially making decisions without access to an expert and without the ability to consult their client but this seems to me to be the appropriate way to move forward. I anticipate that it will be possible merely by looking at the report to conclude whether further expert input is needed. 

55     Mr Danny Ong very fairly impressed upon me the seriousness of his client’s concerns of providing the Defendant with access to the Plaintiff’s confidential information. In this area of technology, the parties are competitors and hence he said that it was of paramount importance to the Plaintiff that the Defendant should not be placed in a better competitive position than it would have been if this litigation had not been commenced. He indicated that, as a last resort, once the Plaintiff knew what information was to be supplied to the Defendant’s expert or to the Defendant itself and on what terms, it might wish to seek leave to discontinue the action. In these circumstances, I accept that it would be appropriate to defer any order for production or inspection of confidential documents for a short period of time for the Plaintiff to assess its position. 

**Matters in dispute on the Order** 

56     A draft order has been drawn up following the hearing and two matters arising have not been agreed upon between the parties. First, there was a limited dispute on the the list of issues to be considered by the Plaintiff’s expert witness. This has now been settled by the Court on the basis of written submissions. Secondly, the precise background and experience of the Defendant’s officer referred to in [52] could not be agreed upon and, again, I have received written submissions. 

57     The dispute centres on the degree of expertise that the officer should have in computer programs, systems and software, more specifically in those for algorithmic trading. The Plaintiff contends that (s)he should not possess any expertise in those fields whereas the Defendant contends that it is sufficient if the person has not been involved in the writing of such material. The difficulty as I see it in the Plaintiff’s contention lies in the lack of clarity surrounding the ambit of the word “expertise” The Defendant’s business involves running a computer operated trading platform. Any executive is likely to have some knowledge about how the system works. When such knowledge becomes “expertise” must be a grey area. 

58     The important considerations are that the person in question must, on the one hand, be able to understand the relevance of the Plaintiff’s expert report to the action yet, on the other hand, his or her possession of the confidential information should not jeopardise that confidentiality or restrict his or her future career. The person should be a person of probity who has not been involved in writing computer programs and is prepared to undertake not to be so involved in the future. 

59     Accordingly the Defendant’s proposed representative: 

 (a) shall possess sufficient seniority to understand the relevance of the Plaintiff’s expert report to the action when explained to him by the Defendant’s lawyers or independent expert (if any); but 


(b) shall not have been or be involved in the writing of computer programs, systems and/or software, in particular for algorithmic trading, and 

(c) shall be prepared to undertake not to be so involved in the future. 

 Copyright © Government of Singapore. 


Source: [link](https://www.singaporelawwatch.sg/Portals/0/Docs/Judgments/[2018] SGHC(I) 4.pdf)
