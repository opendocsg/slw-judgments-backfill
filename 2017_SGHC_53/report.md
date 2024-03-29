# National University Hospital (Singapore) Pte Ltd v Cicada Cube Pte Ltd 



**Case Number** :Originating Summons No 239 of 2015 

**Decision Date** :14 March 2017 

**Tribunal/Court** :High Court 

**Coram** :Aedit Abdullah JC 

**Counsel Name(s)** :Tan Tee Jim, SC, Christopher de Souza, and Darrell Wee (Lee & Lee) for the plaintiff; N Sreenivasan, SC, Andrew Heng and Ivan Qiu (Straits Law Practice LLC) and Jevon Louis (Ravindran Associates) for the defendant. 

**Parties** :National University Hospital (Singapore) Pte Ltd — Cicada Cube Pte Ltd 

_Patents and Inventions_ – _ownership_ 

_Patents and Inventions_ – _employee’s invention_ 

[LawNet Editorial Note: The appeals from this decision in Civil Appeals Nos 138 and 139 of 2016 were dismissed by the Court of Appeal on 28 August 2018. See <span class="citation">[2018] SGCA 52</span>.] 

14 March 2017 

**Aedit Abdullah JC:** 

**Introduction** 

1       What was at stake in the present case was the ownership and recognition as inventors of a patented process (“the Patent”) for the collection of laboratory specimens. Who came up with the invention was strongly disputed between the parties: the defendant, a software engineering company, argued that its officers came up with the invention, almost on the back of the proverbial envelope while brainstorming; the plaintiff, on the other hand, claimed that its employees, including a senior doctor, had developed the idea after years of experience in medical testing. 

2       The registered proprietor of the Patent was Cicada Cube Pte Ltd (“Cicada”), and the named inventors were Cicada’s founders and directors, Dr Anil Kumar Ratty (“Dr Ratty”) and Dr Danny Poo (“Dr Poo”). The National University Hospital (Singapore) Pte Ltd (“NUH”) contended that its employees, Dr Sunil Kumar Sethi (“Dr Sethi”) and Peter Lim, were the ones who had actually came up with the invention disclosed in the Patent (“the Invention”), and that it was therefore the rightful owner of the Patent. 

3       The dispute fell primarily on the determination of who contributed to the inventive concept, or the “heart”, of the Invention. After hearing the parties and considering the evidence, I found that there were in fact two inventive concepts embodied in the Invention. I was persuaded that one of the inventive concepts was contributed by Dr Sethi (although not Peter Lim). NUH failed, however, to discharge its burden of proving that Dr Ratty and Dr Poo did not contribute to the other inventive concept. Accordingly, I ordered that Dr Sethi, Dr Ratty and Dr Poo be named as joint inventors of the invention, and for NUH to be named as a joint proprietor of the Patent together with Cicada. Both parties are dissatisfied with the decision and have appealed. 


**Background** 

**_The parties_** 

4       The plaintiff, NUH, was a Singapore-incorporated company that operated a tertiary hospital. Until 2008, it was part of a group of healthcare institutions known as the National Healthcare Group (“NHG”). Since 2008, it had been a member of an agglomeration called the National University Health 

System [note: 1]. Dr Sethi held the position of Chief of NUH’s Department of Laboratory Medicine 

between 1 July 2002 and 31 March 2016 [note: 2] , whereas Peter Lim was NUH’s Principal Medical 

Technologist at the material time [note: 3]. 

5       The defendant, Cicada, was founded by Dr Ratty and Dr Poo, who were both directors of Cicada at the material time. 

**_Events leading up to the Invention_** 

6       In 2004, the NHG embarked on a project to digitise the clinical care processes in its hospitals (including NUH). At that time, NUH had a mixture of manual and electronic processes for its clinical care workflows. For instance, laboratory tests ordered by doctors for patients were done manually on hardcopy forms and subsequently keyed into an electronic system called the Laboratory Information System (“LIS”). The digitisation project contemplated the development of an Electronic Medical Records (“EMR”) system to computerise records generated and/or stored within NHG’s hospitals. In relation to the specific workflow of the doctor’s order for specimen testing in the laboratory, the plan was that there should be a Computerised Physician Order Entry (“CPOE”) which could enable doctors 

to order medication, laboratory and radiological tests electronically [note: 4]. To that end, a request for proposal was called by NHG sometime in 2004 to solicit proposals for an EMR system with CPOE capability. A vendor was eventually appointed in June 2005 for the supply and implementation of the 

EMR system [note: 5]. 

7       According to NUH, despite implementation of an EMR system, it realised that an additional component, namely, one pertaining to sample collection, was required in order to have in place a complete electronic laboratory trail from test ordering right through to result reporting. NUH decided to develop a software for this purpose. One of the various relevant workflows that needed to be translated to code and made to work with both the EMR and the LIS was the printing of test tube 

labels when specimens were taken from patients and registration of the specimens to the LIS [note: 6] 

. Cicada was subsequently appointed by NUH to develop a software in a project called the Advanced 

Test Ordering Management System (“ATOMS”) [note: 7]. 

8       As NUH did not have sufficient funds for the ATOMS project, Cicada applied for and successfully obtained external funding from the Prime Minister’s Office (“PMO”) through its The Enterprise Challenge (“TEC”) program. Subsequently, a tripartite agreement (“the TEC Agreement”) was entered between Cicada, NHG, and the PMO for Cicada to leverage on the expertise and 

resources of NHG and NUH to conduct pilot trials of ATOMS [note: 8]. 

**_The Patent_** 

9       On 14 August 2007, Cicada filed an application to register the Patent. The Patent was granted by the Intellectual Property Office of Singapore (“IPOS”) on 30 July 2010. It was titled “Laboratory 


Specimen Collection Management System” and named Dr Ratty and Dr Poo as the inventors [note: 9]. 

10     The specification of the Patent described the Invention disclosed therein as “a laboratory specimen collection management system for the clinical laboratory, and especially, a system to identify the type and number of tubes to use to collect patient specimens for testing by the 

laboratory analy[s]er and facilitate the collection of the specimens at the point of care” [note: 10]. 

11     The specification then listed three problems with the existing system for the management of 

laboratory specimen collection [note: 11] : 

 (a) Specimen collection required a specimen taker to determine, before taking the specimen, the type of tube, number of tubes, and the amount of specimen to be collected in each tube. This was not a simple exercise and required experiential knowledge on the part of the specimen taker. The specimen taker would usually consult a chart for each of the specimen test orders ordered by a doctor. However, as there were a number of different permutations in tube selection, the process was tedious and error-prone, compromising patient safety. 

 (b) Specimens collected at the point of care were labelled to identify them with the patients providing the specimens. As the labels were non-standard labels pre-generated en masse and applied to the tubes when the specimens were collected, errors where a tube became labelled with a wrong patient identification could occur. 

 (c) When the specimens arrived at the laboratory, a new set of labels, containing such information as the accession number essential for the laboratory analysis process, would be generated and affixed to each tube. In other words, there would be two labels for each tube of specimen collected (one affixed at the point of collection and another affixed at the laboratory). The need to print and affix two labels per tube was time-consuming, inefficient, and also errorprone. 

12     The specification then averred that the Invention was a laboratory specimen collection management system which comprised a number of specimen collection stations coupled to a specimen 

processing system [note: 12] : 

 (a) The specimen processing system contained the business logic for determining the specimen requirements including the type of tube, number of tubes, colour code of the tube, and the amount of specimen to be taken for each patient. It had a processing unit that was coupled to a database containing, among other information, the laboratory analyser test accession numbers for specimens. 

 (b) The specimen collection stations were located at the point of care and were used by clinicians to collect samples. Each consisted of a user interface device, a hand-held scanner or data input device, a processing unit, and a printer. Patients were identified and verified electronically via the hand-held scanner. The specimen tests ordered by the doctors were displayed graphically on the user interface and this informed the specimen taker of the specimen requirements for the test order (the type of tube, number of tubes, colour code of the tube, and the amount of specimen to be taken for each patient, as determined by the specimen processing system). For each tube, a label would be printed in situ and this contained all the essential information such that in all, only one label had to be affixed onto each tube (as opposed to two labels per tube under the existing system). 


13     According to the specification, the Invention offered the following advantages over the existing system: 

 (a) Since information on the tubes to be used for the collection of specimens was controlled by the system, this helped to ensure that the correct types and number of tubes were used for the collection, thereby ensuring patient safety and improving efficiency in specimen collection. 

 (b) Since the labels were printed in situ at the point of care, chances for label mix-up and errors were reduced, again enhancing patient safety. 

14     The Patent was accompanied by several diagrams. In particular, FIG. 1 showed a number of specimen collection systems connected to a set of specimen processing system via the internet. FIG. 4 gave a schematic view of various components of the specimen processing system, such as (a) a listener server that listened to incoming messages bearing information about specimen orders from a computerised clinician ordering system; (b) a database server that stored the incoming messages; (c) a user interface; (d) a laboratory analyser connector that coupled the specimen processing system to the laboratory analyser; and (e) a “proprietary processing logic”, stated to be “the heart of the 

specimen processing system”, that controlled the behaviour of the specimen processing system [note: 13]. FIG. 1 and FIG. 2 are reproduced below. 

15     The Patent comprised a number of claims, set out at [63] below. 

**Procedural History** 


16     On 27 July 2012, NUH filed a reference to the Registrar of Patents (“the Registrar”) pursuant to 

s 47(1) of the Patents Act (Cap 221, 2005 Rev Ed), for the following orders: [note: 14] 

 (a) that NUH be named as the sole and rightful proprietor of the Patent, in place of Cicada; and 

 (b) that Dr Sethi be named as the sole and rightful inventor of the Invention disclosed in the Patent, in place of Dr Ratty and Dr Poo. 

17     On 18 February 2015, pursuant to s 47(8) of the Patents Act, the Registrar issued a decision declining to deal with the reference, on the basis that the reference would more properly be 

determined by the court as the matter was “complex” [note: 15]. 

18     On 17 March 2015, NUH commenced the present OS proceedings for, among other things, the 

following orders [note: 16] : 

 (a) that NUH be named as the sole and rightful proprietor of the Patent in place of Cicada; and 

 (b) that Dr Sethi and Peter Lim be named as the rightful inventors of the Patent in place of Dr Ratty and Dr Poo. 

19     On 10 July 2015, NUH applied for, and obtained, leave to amend the OS to seek the following orders: 

 (a) that NUH be named as the sole and rightful proprietor of the Patent in place of Cicada or, alternatively, as the joint proprietor of the Patent together with Cicada; and 

 (b) that Dr Sethi and/or Peter Lim be named as the rightful inventor(s) of the Patent in place of Dr Ratty and Dr Poo or, alternatively, as the joint inventor(s) of the Patent together with Dr Ratty and Dr Poo [note: 17]. 

**NUH’s case** 

20     According to NUH, the inventive concepts of the Invention were [note: 18] : 

 (a) a specimen processing system which determined, through a “business logic”, the specimen requirements for the specimen test orders (“Determination Concept”); and 

 (b) the graphical display of the specimen requirements at a specimen collection station (“the Graphical Display Concept”). 

21     NUH contended that the Patent rightfully belonged to it as its employee, Dr Sethi, was the one who had formulated the inventive concepts in the course of his employment as the Chief of NUH’s Department of Laboratory Medicine. Dr Sethi was assisted by Peter Lim, who was also NUH’s employee at the material time and who was, “in substance”, jointly responsible with Dr Sethi for devising the 

Inventive Concepts [note: 19]. 

22     Based on NUH’s version of the events, Dr Sethi was alive to the problems with the pre-existing system of laboratory specimen collection outlined in the Patent (see [11] above) and had, sometime in the middle of 2004, came up with “some sort of conception of what the electronic solution to the 


problems might be” [note: 20]. He decided to pursue that solution as part of NUH’s ambitious digitisation project (see [6] above). This required a software. Although NUH could have developed the software in-house, the Information Technology Department of the NHG was rather occupied at that 

point in time, which was in June 2005, and could not spare the resources [note: 21]. As a result, NHG appointed Cicada to develop the software based on information and parameters provided by NUH/NHG. Subsequently, NHG and Cicada entered into a Memorandum of Understanding on 16 December 2005 to 

develop what became known as ATOMS (see [7] above) [note: 22]. 

23     With respect to the proposal to the PMO to apply for funding under the TEC programme (see [8] above) (“the TEC Proposal”), Dr Sethi maintained that Cicada, being merely a software company, did not have the wherewithal to put together the proposal on laboratory management and specimen collection replete with references to academic journals in this field. He was the one who put together the TEC Proposal. Cicada was, however, listed as a co-proposer in the TEC Proposal, only because one of the prerequisites of the TEC was that the proposal must include a private sector participant [note: 23]. 

24     In the course of engaging Cicada to write the software for ATOMS, NUH shared with Cicada what later became the inventive concepts of the Patent. Cicada then surreptitiously applied for and obtained the Patent that encompassed the pre-existing and envisioned workflows and processes of NUH’s laboratory specimen collection management system which it became aware of during the 

development of the software [note: 24]. Although NUH was aware that Cicada had filed for a patent in 2007 in connection with the ATOMS project, it had always been its understanding that the patent was only for the software that Cicada developed and not a process patent. It only realised that the Patent was a process patent in 2011 and hence commenced proceedings for determination of the inventorship and proprietorship of the Patent shortly after. 

**Cicada’s case** 

25     According to Cicada, the inventive concept of the Invention is the integration of a front-end test ordering system such as the CPOE with a back-end laboratory information system, so as to eliminate errors such as mislabelling of test tubes, inadequate collection of specimen samples and use of wrong test tubes, by doing the following two things at the same time and place: 

 (a) collating information on the specimen collection requirements based on the specimen test ordered and then graphically displaying the specimen collection requirements; and 

 (b) generating a unique laboratory accession number, which also contained patient information, in a single label to be affixed on the specimen collection test tube [note: 25]. 

26     The CPOE and the Sample Volume Metrics (“SVM”) (see [68] below) _per se_ were not part of the 

said inventive concepts [note: 26]. 

27     Cicada claimed that Dr Ratty and Dr Poo were the ones who had come up with the abovementioned inventive concepts, and so were rightly named as joint inventors in the Patent. It was not disputed that Dr Sethi and Dr Ratty had been childhood friends for about 50 years and would meet up regularly for chats on various issues. According to Dr Ratty, during one of these chats which happened in the latter half of 2004, Dr Sethi alluded to the impact of laboratory errors in specimen 

collections in hospitals [note: 27]. Dr Ratty made a mental note of the problems raised by Dr Sethi and subsequently had a discussion with Dr Poo, who had substantial IT engineering experience. After 


brainstorming, Dr Ratty and Dr Poo jointly devised a solution to the problems [note: 28]. By the end of 2004, Dr Ratty informed Dr Sethi that he had conceived of a solution to address the problems faced 

by Dr Sethi and presented the solution to Dr Sethi in the form of ATOMS [note: 29]. As Dr Sethi informed Dr Ratty that NUH had no funds to implement the solution, Dr Ratty explored funding through 

the PMO’s TEC program [note: 30]. 

28     Cicada further made a number of other arguments, including that Dr Sethi was not an employee of NUH at the material time, and that the present action was subjected to s 47(9) of the Patents Act. 

**The issues** 

29     At some points in the present proceedings, NUH argued that the Patent was not validly registered for want of inventiveness. However, whether or not the Patent ought to be granted or amended in some way was not properly a question before me. What was before me was the issue of to whom the Patent should be granted, and who should be recognised as the inventor or inventors. In answering these questions, I had to take the Patent as it was. 

30     The allegations made by NUH that Cicada had filed the Patent in secrecy were not directly relevant in the present proceedings either, except in so far as they might form part of the background for the question of who had contributed to the inventive concept(s) of the Invention to be addressed. 

31     What I had to consider were as follows: 

 (a) what was/were the inventive concept(s) of the Invention disclosed in the Patent; 

 (b) who contributed to the inventive concepts; and 

 (c) who was/were the rightful owner(s) of the Patent. 

32     Further, I had to determine a preliminary issue raised by the parties on whether the present proceedings were subject to s 47(9) of the Patents Act, and also questions raised by Cicada concerning Dr Sethi’s status as an employee of NUH at the material time. 

**The decision** 

33     I found that the present proceedings before me were not subject to s 47(9) of the Patents Act. 

34     In establishing who the rightful owner of the Patent was, the principles that could be distilled from the relevant case law interpreting the Patents Act or provisions that were _in pari materia_ were that the court should identify who contributed to the inventive concept, or what had been described as the “heart”, of the Invention. 

35     In determining what the inventive concept of an invention was, the court must look at the patent as a whole. In doing so, the court was entitled to examine both the claims and descriptions, bearing in mind the purpose of each part of a patent application. I was of the view that in construing the inventive concept of a patent, it might be that there were in fact several such concepts encompassed within a single patent; in that regard, there might not be a single “heart” of the invention as such. 


36     Further, it had been said that where an inventive concept consisted of a combination of elements, it was the person who had come up with the actual combination who ought to be credited as having contributed to the inventive concept of the invention, and not those who might have created the individual elements. That was to my mind correct in so far as it could be specified who had come up with the combination as a whole. However, in some cases, the combination might not be the product of a single inventor. 

37     In the present case, I was of the view that there were two inventive concepts within the Invention disclosed by the Patent. In this, my finding differed from the position of either party. The two inventive concepts were: 

 (a) the linkage or interaction between what was done in the ordering of a medical test ( ie , the processes for ordering tests), and what was done at the specimen-taking side ( ie , the processes for collecting specimens), so that, adopting the language of operations management or quality assurance, errors or mistakes were prevented (“the 1st Inventive Concept”); and 

 (b) the specification for the taking of specimens, ie , among other things, how the system actually ensured identification or determination of relevant constraints (such as the type of tube, number of tubes, and the amount of specimen to be collected in each tube) in each case, and the process of actual interaction or communication of different components of the system, including information processing and the display of the specification to the clinician taking the specimens (“the 2nd Inventive Concept”). 

38     With respect to the 1st Inventive Concept, I was satisfied that this was, on the evidence before me, invented by Dr Sethi. While there was an absence of a single contemporaneous record clearly showing a specific and definite point by which Dr Sethi came up with the 1st Inventive Concept, I was satisfied that this was done before the involvement of Dr Ratty and Dr Poo. In particular, I was satisfied that the handwritten note of Dr Ratty capturing the integration of the various components of the system was something that arose after Dr Sethi’s creation of the idea of linking the various components. 

39     As for the 2nd Inventive Concept, I was in the end not persuaded that NUH had shown that Dr Ratty or Dr Poo did not come up with it. The focus of the arguments and the evidence that was put before me was really elsewhere. I could not say that Dr Poo’s contribution in terms of coding what was required was not inventive or did not touch on the 2nd Inventive Concept. As for Dr Ratty, his contribution was perhaps less tangible or apparent than Dr Poo’s but again I could not conclude that this contribution did not involve any invention or contribution to the 2nd Inventive Concept. 

40     In contrast, I noted that while Mr Peter Lim might have made a contribution to the better functioning of the Invention, his contribution was not to the inventive concepts but was to a particular mode of facilitating the working of these inventive concepts. The line between an inventive concept and a mode or way of implementing that inventive concept was not capable of being specified in an abstract way. All would depend on the facts. 

41     Finally, as regards the employment status of Dr Sethi, I would emphasise that even in the absence of opposition by Cicada, the onus was on the claimant (NUH in this case) to ensure that the elements of its claim were satisfied. On a review of further submissions of the parties and affidavits filed, I was satisfied that Dr Sethi was employed by NUH at the material time. While there was a contract between him and the National University of Singapore (“NUS”), he was also in a contract of employment with NUH, and in respect of the activities in issue in the present case, he was answerable to the control and supervision of NUH. It could be stated conversely that he was not a 


contractor or supplier of services to NUH. Furthermore, the courts would need to recognise that there was a strong innovative role inherent in many jobs these days, even if it was not explicitly mentioned within the normal or day-to-day job scope. All employees, whether in the public or private sector, whether managerial or clerical, were expected to contribute to the organisation by proposing innovations or improvements. What counted as being within the scope of employment had to be seen in that light. 

**Analysis** 

**_Preliminary issue – whether the present proceedings were subject to s 47(9) of the Patents Act_** 

42     Cicada contended that the present Originating Summons were subject to s 47(9) of the Patents Act. 

43     Section 47(1) of the Patents Act provided that after a patent had been granted, any person having or claiming a proprietary interest in or under the patent may refer to the Registrar the question of whether the patent had been rightly granted to the right person(s). Section 47(5) provided that the Registrar was not to make any order transferring a patent on the ground that the patent was granted to a person not rightly entitled to it, if the question of whether the patent had been rightly granted to the right person(s) was referred to it pursuant to s 47(1) more than two years after the date of grant of the patent, unless it was shown that the person registered as the proprietor of the patent knew at the time of the grant that he was not entitled to the patent. Section 47(5) of the Patents Act was not directly relevant in this case as the Patent was granted on 30 July 2010 and NUH had filed the reference to IPOS on 27 July 2012, within (although just barely) the two-year period. 

44     An issue arose under s 47(9) of the Patents Act, however, because the Registrar, pursuant to s 47(8), declined to deal with the reference on the basis that it would more properly be determined by the court. The Registrar made this decision on 18 February 2015. Shortly thereafter, on 17 March 2015, NUH commenced the present OS. By that time, as more than two years had already passed since the grant of the Patent, the issue that came up was then whether the OS proceedings were caught by s 47(9) of the Patents Act, which read as follows: 

 The court shall not in the exercise of any such declaratory jurisdiction determine a question whether a patent was granted to a person not entitled to be granted the patent if the proceedings in which the jurisdiction is invoked were commenced after the end of the period of 2 years beginning with the date of the grant of the patent, unless it is shown that any person registered as a proprietor of the patent knew at the time of the grant or, as the case may be, of the transfer of the patent to him that he was not entitled to the patent. 

 [emphasis added] 

45     The issue rested upon the proper interpretation of the words “the proceedings in which the jurisdiction is invoked”. In a situation such as the present, did “the proceedings in which the jurisdiction is invoked” refer to the original reference that was first brought to the Registrar pursuant to s 47(1), or did it refer to the present OS proceedings that NUH brought after the Registrar declined to deal with the reference? I was of the view that the former interpretation must be the correct one. In situations such as the present, the plaintiff could only file the OS proceedings in the court after the Registrar had issued its decision concerning the reference made to it, and the plaintiff had no control over how long the Registrar would take to issue its decision. In this case, the Registrar took 


more than two and a half years before it decided to decline to decide on the reference. It would be unfair to a plaintiff if, for no fault of its own, it became subjected to the additional requirement of having to prove that the registered proprietor of the patent knew at the time of the grant that he was not entitled to the patent under s 47(9) of the Patents Act, which it otherwise would not have had to prove had the Registrar not declined to decide on the reference that the plaintiff had filed. This could not have been the intention of Parliament in enacting the said provisions in the Patents Act. 

46     I would, however, add a caveat to the above. In situations described above, if the relief sought in the OS proceedings in the court were to differ materially from that sought in the original reference t o the Registrar, then the OS proceedings must be taken as fresh proceedings detached from the original reference to the Registrar. In such cases, if the OS proceedings were commenced more than two years after the date of the grant of the patent, then s 47(9) of the Patents Act would be attracted, regardless of whether or not the original reference to the Registrar was filed within or after the two year period. In this case, the relief sought by NUH in the reference to IPOS and in the OS proceedings were essentially the same. In both cases, NUH was seeking to be named as a rightful proprietor of the Patent, and for its employee(s) to be named as the rightful inventor(s). There were some differences in the relief sought in the reference and in the OS proceedings to the extent that in the reference to the Registrar, NUH asked for it to be named as the sole rightful proprietor of the Patent, but later included in the OS an alternative prayer for it to be named a co-proprietor of the Patent alongside Cicada (see [16]-[19] above). The other difference was that NUH originally asked for Dr Sethi to be named as the sole rightful inventor of the Invention, but later included in the OS an alternative prayer for Dr Sethi and/or Peter Lim to be added as joint inventors together with Dr Ratty and Dr Poo. Nonetheless, while there were differences, they related only to the extent of relief sought. The nature or kind of the relief sought in the OS remained the same as that sought in the reference to the Registrar. 

47     Given the above, I decided that s 47(9) of the Patents Act did not apply in the present OS proceedings before me. 

**_General principles on inventorship and ownership_** 

48     The issue of ownership of a patent was governed by s 19(2) of the Patents Act. Section 19(2) ( _a_ ) provided that a patent may be granted “primarily to the inventors or joint inventors” of the invention, although in situations exclusively set out in s 19(2)( _b_ ) and ( _c_ ), persons other than the inventors might be granted a patent. Section 19(2) is set out below: 

 A patent for an invention may be granted — 

 ( a ) primarily to the inventor or joint inventors; 

 ( b ) in preference to paragraph ( a ), to any person or persons who, by virtue of any enactment or rule of law, or any foreign law or treaty or international convention, or by virtue of an enforceable term of any agreement entered into with the inventor before the making of the invention, was or were at the time of the making of the invention entitled to the whole of the property in it (other than equitable interests) in Singapore; or 

 ( c ) in any event, to the successor or successors in title of any person or persons mentioned in paragraph ( a ) or ( b ) or any person so mentioned and the successor or successors in title of another person so mentioned, 


 and to no other person. 

49     Section 49 of the Patents Act set out the circumstances under which an employer would have ownership of an employee’s invention. In such cases, although the employee remains the rightful inventor of the invention, ownership of the invention vests with his employer. Section 49(1) read as follows: 

 49.—(1) Notwithstanding anything in any rule of law, an invention made by an employee shall, as between him and his employer, be taken to belong to his employer for the purposes of this Act and all other purposes if — 

 (a) the invention was made in the course of the normal duties of the employee or in the course of duties falling outside his normal duties, but specifically assigned to him, and the circumstances in either case were such that an invention might reasonably be expected to result from the carrying out of his duties; or 

 (b) the invention was made in the course of the duties of the employee and, at the time of making the invention, because of the nature of his duties and the particular responsibilities arising from the nature of his duties he had a special obligation to further the interests of the employer’s undertaking. 

50     As to who might be considered the inventor of an invention, s 2(1) of the Patents Act provided that an “inventor”, in relation to an invention, meant “the actual deviser of the invention”. In _Dien Ghin Electronic (S) Pte Ltd v Khek Tai Ting (trading as Soon Heng Digitax)_ <span class="citation">[2011] 3 SLR 227</span> (“ _Dien Ghin_ ”), Chan Seng Onn J adopted (at [13]) the following passage in _Yeda Research and Development Co Ltd v Rhone-Poulenc Rorer International Holdings Inc_ [2008] RPC 1 (“ _Yeda_ ”), where Lord Hoffman was interpreting provisions in the UK’s Patents Act which were _in pari materia_ with the relevant provisions in Singapore’s Patents Act: 

 The word ‘actual’ denotes a contrast with a deemed or pretended deviser of the invention; it means, as Laddie J. said in University of Southampton’s Application [2005] RPC 11 [at] [39], the natural person who ‘came up with the inventive concept’. It is not enough that someone contributed to the claims, because that may include non-patentable integers derived from the prior art: see Henry Brothers (Magherafelt) Limited v Ministry of Defence [1997] RPC 693 at 706; [1999] RPC 442. As Laddie J. said in the University of Southampton case, the ‘contribution must be to the formulation of the inventive concept’... 

51     Thus, the inventor was the natural person who had formulated or contributed to the formulation of the inventive concept. What amounted to contribution to an inventive concept could encompass a number of different types of activities. Summarising the discussion at Lionel Bently and Brad Sherman, _Intellectual Property Law_ (Oxford University Press, 4th Ed, 2014) (“ _Bently and Sherman_ ”) at pp 598 and 599, the following could amount to contributions to the inventive concept: 

 (a) solving or helping to solve a particular problem or answering a particular question; 

 (b) improvement of an answer previously developed; and 

 (c) the formulation of the problem that was addressed. 

However, just because an activity or type of contribution fell within the above did not mean that it _ipso facto_ amounted to a contribution to the inventive concept of an invention: an assessment still 


had to be made against the context. While certain contributions (such as posing of the problems to be solved or the answering of these problems) were usually treated as being inventive, other contributions (such as the supply of the test tubes used in the experiments) would usually be regarded as being non-inventive. In between these two extremes there was a range of other types of contributions that were more difficult to categorise. The question that arose here was which of the various contributions that had been made towards the production of an invention ought to be recognised as being inventive (or technically creative) and which ought not to be recognised as such. This was a particularly complex issue, not least because what is considered to be inventive not only changes over time, but also changes between different areas of science and technology: see _Bently and Sherman_ at p 598. 

52     Where more than one natural person played a role in the formulation of the inventive concept, each of these persons would all be inventors of the invention. Further, where an inventive concept consisted of a combination of elements, it was the person who had, in substance, come up with the actual combination who ought to be credited as having contributed to the inventive concept of the invention. In this regard, I respectfully adopted the following passage of Jacob J (as he then was) in _Henry Brothers (Magherafelt) Ltd v Ministry of Defence and the Northern Ireland Office_ [1997] RPC 693 (“ _Henry Brothers_ ”) at 706: 

 I do not think it is right to divide up the claim for an invention which consists of a combination of elements and then to seek to identify who contributed which element. I think the inquiry is more fundamental than that. One must seek to identify who in substance made the combination. Who was responsible for the inventive concept, namely the combination?... [Who] turned a useless collection of elements into something which could work[?] 

53     In addition, a person might be a deviser of an invention as claimed, even though he might lack the capability to design or put into place the precise details of how the inventive concept might be realised into a functional product, and had left another person to work out those details: _Dien Ghin_ at [13]. On the contrary, the person who merely did what was suggested to him by the actual deviser did not take part in devising the invention, and is not to be regarded as a joint inventor. In determining joint inventorship, the test was whether the second person could be said to be “in substance” jointly responsible for devising the inventive concept of the patent: _Stanelco Fibre Optics Ltd’s Applications_ [2005] RPC 15 at [18] and [20]. 

54     In the present case, the burden was on NUH to prove that Dr Sethi and Peter Lim had contributed to the inventive concepts of the Invention. The burden of proof was as set out in _Yeda_ (at [21]): 

 [A] person who seeks to be added as a joint inventor bears the burden of proving that he contributed to the inventive concept underlying the claimed invention and a person who seeks to be substituted as sole inventor bears the additional burden of proving that the inventor named in the patent did not contribute to the inventive concept. 

55     What then, was the inventive concept of an invention? The inventive concept had been described as “the heart” of an invention, and in identifying it, the court was essentially “concerned with the identification of the core (or kernel, or essence) of the invention... which entitle[d] the inventor’s achievement to be called inventive”: _Generics (UK) Ltd v H Lundbeck A/S_ [2009] UKHL 12 at [30]. 

56     In construing from a patent what the inventive concept(s) of the invention disclosed therein was, I was of the view that the court was entitled to, and indeed ought to, look at the patent as a 


whole, including the specification as well as the claims. There were some disagreements between the parties in this case on whether the inventive concepts should be gleaned from the information in the patent specification rather than from the claims. I concluded that the approach should be as follows. 

57     First, in proceedings where the court was tasked to determine the extent of protection of a patent, _ie_ , what monopolies were actually claimed and granted, s 113(1) of the Patents Act, as set out below, applied: 

 For the purposes of this Act, an invention for a patent for which an application has been made or for which a patent has been granted shall, unless the context otherwise requires, be taken to be that specified in a claim of the specification of the application or patent, as the case may be, as interpreted by the description and any drawings contained in that specification, and the extent of the protection conferred by a patent or application for a patent shall be determined accordingly. 

Hence, in determining the extent of protection covered in a patent, the claims of the patent were determinative, although the court could use the description and any drawings contained in the specification to interpret what the claims covered. The present proceedings before me did not concern a determination of the extent of protection covered in the Patent. 

58     Secondly, in entitlement proceedings such as the present where the court was required to determine what the invention disclosed in a patent was and who contributed to the inventive concepts of the invention, the claims of a patent were not conclusive. In _Markem Corp v Zipher Ltd_ [2005] RPC 31 (“ _Markem Corp_ ”), the English Court of Appeal had to deal with questions of entitlement before the patent was granted. There, the court observed (at [100]) that the question of entitlement could arise before any claims existed, and in principle that question must remain the same regardless of whatever claims that might later emerge. In such cases, the court had this to say (at [102]) with respect to the approach that should be taken in determining who contributed what to the inventive concept and what rights if any they had in the invention: 

 It is not possible to be very specific about how this is to be done. But as a general rule one will start with the specific disclosure of the patent and ask whether that involves the use of information which is really that of the applicant, wholly or in part or as joint owner... [W]hat one is normally looking for is “the heart” of the invention. There may be more than one “heart” but each claim is not to be considered a separate “heart” on its own. 

59     The present case did not involve questions of entitlement over a patent that had not yet been granted. The Patent in this case was granted in 2010. In _Statoil ASA v University of Southampton_ (BL O/204/05), the tribunal observed (at [38]) that in determining what the inventive concept(s) of an invention was, even in a granted patent, the court must look at the information in the specification rather than simply looking at the monopoly claimed, although this did not mean that the court was not to look at the claims at all. In my view, this must be correct. There was a fundamental difference between what was considered an invention on one hand, and what monopoly an inventor chose to obtain on the other hand. In _First Currency Choice Pte Ltd v Main-Line Corporate Holdings Ltd and Another Appeal_ <span class="citation">[2008] 1 SLR 335</span>, the Court of Appeal cited (at [23]) the following passage of Laddie J in _Merck & Co Inc v Generics (UK) Ltd_ [2004] RPC 31: 

 The purpose of a patent is to convey to the public what the patentee considers to be his invention and what monopoly he has chosen to obtain. These are not necessarily the same. The former is primarily to be found in the specification [ ie , the description] and the latter is primarily to be found in the claims. 


An inventor was free to exclude an inventive concept of his invention from the scope of monopoly claimed if, for whatever reason, he so wished. Hence, the claims were not determinative when a court had to decide on the question of what the inventive concepts of an invention were, although the court should take them into account, together with the specification. 

**_Issue 1: What was/were the inventive concept(s) of the Invention_** 

60     With the above principles in mind, I proceeded to determine what the inventive concept(s) of the Invention was/were, by construing the Patent as a whole. I considered all the key features of the Patent, as set out in [10]–[15] above, and I concluded that there were two inventive concepts within the Invention disclosed in the Patent (see [37] above). 

61     My conclusions differed from the contentions put forward by each side in relation to the inventive concepts. NUH argued that there were two: the Determination Concept, _ie_ , the specimen processing which determined, through a “business logic”, the specimen requirements for the specimen test orders; and the Graphical Display Concept, _ie_ , the visual display of these requirements (see [20] above). Cicada, for its part, contended that the inventive concept was the integration of front-end test ordering with back-end information, eliminating errors by collating and graphically displaying the requirements and generating a single label containing the accession number and patient information for each tube (see [25) above). Neither conception to my mind properly captured the inventive concept(s) of the Invention. In particular, in my view, the “business logic”, _ie_ , a system or heuristic parameters that captured a method of dealing with the data, and the graphical display of the specimen requirements, might have been particular modes of facilitating the working of the Invention, but they were not the inventive concepts, or the “hearts” of the Invention, for reasons that are elaborated upon below. As for the generation of a single label for each tube, this, in my view, was a consequence that flowed from the linkage or interaction between the processes for ordering tests and the processes for collecting specimens ( _ie_ , the 1st Inventive Concept that I identified), rather than part of an inventive concept itself. 

62     Several considerations led me to my identification of the 1st and 2nd Inventive Concepts. First, the Patent disclosed three key problems with the existing system (see [11] above). The first problem (see [11(a)] above) pertained to the difficulty faced by a specimen taker in determining the type and number of tubes to use and the amount of specimen to be collected in each tube. The second and third problems related to the need to affix two labels on each tube and the possibility of mislabelling (see [11(b)] and [11(c)] above), but, in my view, the underlying issue was really the need for tests ordered for each patient to be correctly administered by ensuring that patients were correctly identified at the point of specimen taking and that the specimens collected from them were accurately labelled as having come from particular patients. Errors might arise due to the lack of interaction between the test ordering side and the specimen taking side, such that information on what test was ordered for each patient was not transmitted accurately to the specimen taking side. As a hospital, NUH must have had an existing system for ordering tests, an existing system for taking specimens for the tests, and an existing system for downstream processing of the specimens, even prior to the Invention. The details of each of these systems were not important; what mattered was that based on the evidence, those systems operated as more or less discrete units with little integration between them. The inventive concepts must address the problems identified. 

63     The claims in the Patent and the diagrams (especially FIG. 4) also led me to my conclusion on the 1st Inventive Concept. The claims that I found most relevant for the present purpose are reproduced below: 

 (Claim 1) A laboratory specimen collection management system comprising a specimen test 


 ordering system having functional features for entering specimen test orders; a specimen collection station having a bar-code scanner or data input device for capturing the identity of the patient providing specimens; a specimen processing system in communication with the specimen collection station and coupled to a database, wherein the specimen processing system determines the specimen requirements for the specimen test orders to be graphically displayed at the specimen collection station; a specimen receipt system; and a laboratory information system. 

 (Claim 2) A system according to claim 1, wherein specimen test orders are entered into the specimen test ordering system; information in a specimen test order includes patient unique identification code, the specimen test ordered, the unique identity code of the person ordering the specimen test, and the location where the specimen test is ordered. 

 ... 

 (Claim 5) A system according to claim 1, wherein the specimen collection station retrieves from the specimen processing system the patient unique identification code, the specimen test ordered, the unique identity code of the person ordering the specimen test, and the location where the specimen test is ordered, the specimen test collection station displays graphically on a user interface the type of tube, number of tubes, colour code of the tube and the amount of specimen to take for the identified patient, the specimen test collection station prints in situ for each tube displayed a bar-code label or any form of digitally readable label containing the patient identification code, patient name, the unique laboratory analy[s]er test accession number for a specimen, the date and time of print, location, test codes and colour of tube. 

 ... 

 (Claim 8) A system according to claim 1, wherein the specimen test ordering system also sends to the specimen processing system patient unique identification code, the specimen test ordered, the unique identity code of the person ordering the specimen test, and the location where the specimen test is ordered to indicate an order has been made. 

I was of the view that the above claims clearly established a linkage between the test ordering side and the specimen taking side as a key part of the invention for which monopoly was claimed. There was a flow of information including the patient unique identification code and the specimen test ordered (which were critical information for ensuring that specimens were collected from the correct patient for the correct test) from the test ordering system to the specimen processing system, and then from the specimen processing system to the specimen collecting stations situated at the specimen taking side. Such flow of information addressed head-on the issue underlying the second and third problems identified in the Patent (see [11] above). 

64     Similarly, as stated in [14] above, FIG. 4 described the specimen processing system, which was a major component of the Invention, as being made up of “a listener server” that listened to incoming messages bearing information about specimen orders from a computerised clinician ordering system. The specimen processing system was, in turn, coupled to the specimen collection stations which were situated at the specimen taking sites. 

65     But the linkage of the test ordering side and the specimen taking side only solved some of the problems. The difficulty faced by a clinician taking the specimens in determining the type and number of tubes to use, and the amount of specimen to be collected in each tube, was a major problem specifically highlighted in the Patent (see [11(a)] above). I considered it significant that at the time of applying for the Patent, the prior art did not teach or suggest an automated system which 


## Q. 

## A. 

## Q. 

## A. 

## ... 

determined the specimen requirements for test orders, but required clinicians taking the specimens to first obtain from the laboratory “draw lists” instructing which test samples must be taken from the patients. The clinician had to use his or her experiential knowledge to determine the requirements for each test. The Invention was different because, as stated in specification [0007], its specimen processing system contained a “business logic” for determining the specimen requirements. The specimen requirements, automatically determined, were then communicated to the clinician taking the specimens when they were graphically displayed at the specimen collection stations. I was therefore of the view that how the system actually determined the specimen requirements, and processed and relayed these requirements to the clinician taking the specimens, was an inventive concept of the Invention. 

66     Before me, the parties argued that graphical display of the specimen requirements on the user interface of the specimen collection station was an inventive concept. I was not so persuaded. The essence of the inventive concepts, as identified, was in the linkage of the various systems and processes and the relay of information. How exactly the information was relayed was not critical, and graphical display was but one mode for relaying the specimen requirements, as determined by the specimen processing system, to the clinician taking the sample. The distinction between an inventive concept, and what was no more than a particular mode or way of implementing that inventive concept, was not capable of being specified in an abstract way. All would depend on the specific facts. 

67     I also could not agree with NUH that the SVM was part of the inventive concept. NUH claimed that the SVM had two aspects – a logic and a database. The database fitted into the logic to determine the specimen requirements that would then be graphically displayed to the clinician taking 

the specimen [note: 31]. According to NUH, this logic that was part of the SVM was the same “business logic” (see [12(a)] above) and “proprietary processing logic” (see [14] above) that was stated in the Patent to be “the heart of the specimen processing system”. Further, Peter Lim stated in his statutory declaration that this logic that was part of the SVM was reflected in certain 

Powerpoint slides that he had done up [note: 32]. However, having reviewed the said Powerpoint slides, it was not apparent to me that they represented the type of “logic” that Peter Lim said they did. In my view, the Powerpoint slides showed no more than data on volumes of specimens (blood) to be taken for different test. I accepted Cicada’s contention that the SVM was no more than a dataset which represented the optimisation of the specimen collection requirements (particularly the volume of 

specimen to be collected) [note: 33]. I noted that Dr Sethi appeared to have conceded this point 

during cross-examination. An extract of the Notes of Evidence is provided below [note: 34] : 

 At its most basic version, the SVM was nothing more than a table, am I right? 

 Sir, the SVM was an Excel Sheet, yes. 

68     The SVM dataset was no more than a compilation of data, as specified by the manufacturers of the testing machines used by NUH, on the amount of blood that needed to be drawn and other specimen requirements for each test. Dr Sethi’s evidence was as such during cross-examination: 

 Of course. What type of test tube you use which is coated with what substance would depend on the test and would depend on the machine you have, am I right? 

 Yes, your Honour [note: 35]. 


## Q. 

## A. 

## ... 

## Q. 

## A. 

 COURT: In terms of the database, the SVM data set, what did you do to develop that? 

 A. The dataset is merely the test specification for each orderable test at NUH, so it’s just a listing for tests. Then we assign arbitrary SVM volumes to each of those. 

 Court: And what did you draw on to develop the logic? How did you actually develop the logic, really? Just through your own thinking and experience or did you – 

 A. I was trying to mimic human thinking using those codes, okay to – so that – but at the same time I want the user to have the experience where they will not know what goes behind that screen, so that it’s very user-friendly and what goes behind the screen is actually all those logic that works out – are pushing out those graphics to the user. 

 [...] The amount of blood that’s needed for each test is specified by the manufacturer of the machine, am I right? 

 Yes, your Honour [note: 36]. 

 Now, the machine will have a requirement for each of those tests in terms of amount of blood, type of test tube, and the size of test tube, am I right [note: 37]. 

 Yes, your Honour. 

And the evidence of Peter Lim was as such [note: 38] : 

69     NUH could not adduce any evidence to show that apart from being a dataset, there was a “logic” component to the SVM, _ie_ , a system or heuristic parameters that captured a method of dealing with the data. When asked how he had developed the “logic” he contended he had developed, Peter 

Lim could not give the court a concrete answer [note: 39] : 

70     Thus, all that NUH could prove, at the most, was that the SVM was a dataset of manufacturerdefined specimen requirements. There was nothing inventive in this, and the SVM could not be an inventive concept of the Invention. 

71     I should finally note that the patent in the present case did not to my mind involve a combination of inventive concepts that called for the recognition as inventor of the person who came up with the combination, as noted in the case of _Henry Brothers_. 

**_Issue 2: Who contributed to the inventive concepts?_** 

_The 1st Inventive Concept_ 

72     On the evidence before me, I was satisfied that Dr Sethi was the one who had come up with the 1st Inventive Concept. 


73     It was not disputed that in 2004, the NHG embarked on a project to digitise the clinical care processes in its hospitals (including NUH) (see [6] above). In the early part of 2005, as part of this digitisation initiative, the NHG held a series of meetings to discuss and design the workflows which could be incorporated into NUH’s existing and proposed electronic systems, and to brainstorm for 

solutions to identified problems in the existing workflows [note: 40]. Documentary evidence showed that these meetings produced ideas that coincided with several aspects of the Invention as disclosed in the Patent. For instance, the minutes of a particular meeting held in May 2005 indicated that prelabelling was suggested whereby nurses would affix labels bearing accession numbers onto the tubes 

at the point of collection of the specimens [note: 41]. This suggestion coincided with the notion of _in situ_ printing of labels that was set out in the Patent. Another document, named “CPOE Lab-To-Be”, that was created sometimes in mid-April 2005, elaborated on an electronic workflow for specimen collection and management which involved, among other things, nurses/phlebotomists “scan[ning] patient identification to retrieve laboratory request with instructions for sample collection (type of 

specimen, number of tubes/sample required)” and “request[ing] accession number[s] from LIS” [note: 42]. This coincided with what was reflected in Claim 1 of the Patent (see [63] above). More 

importantly, I was of the view that this was indicative of an idea for linkage of the specimen collecting processes and the test ordering processes, with a relay of information from the latter set of 

processes to the former ( _ie_ , the 1stInventive Concept). It was Dr Sethi’s evidence that he was much 

involved in the brainstorming meetings and that he had vetted the CPOE Lab-To-Be document [note: 43] , and I accepted that as much. 

74     I also considered it significant that a large part of the TEC proposal was drafted by Dr Sethi. It was not disputed that the first draft of this proposal was created by Dr Poo on 16 February 2005. However, he left portions of the draft uncompleted and asked Dr Sethi “to add your parts” to the 

draft [note: 44]. Dr Sethi did so on 1 March 2005. Among other things, Dr Sethi wrote the entire portion of the TEC Proposal on “Project Details”, where he gave particulars of the novel features of the intended system design, and a proposed management workflow for laboratory test orders with details such as _in situ_ printing of labels at the point of specimen collection. Under the “Project Description” section of the TEC Proposal, Dr Sethi wrote about how laboratory information systems “originally deployed to be silos of information, with little need to interact with other systems”, were no 

longer sufficient to meet current needs [note: 45]. He identified the main problem with the current system as being the possibility of errors in test orderings, citing articles which showed that laboratory testing procedure was an important contributor in improper healthcare delivery. He wrote that “today’s laboratory operation require[d] much more”, that there was a need to “[move] away from monolithic LIS to enterprise-wide solutions”, to “push the LIS beyond initial design”, and that “[c]onnectivity and communication [were] critical components for laboratory success”. This strongly suggested to me that Dr Sethi was the one who had come up with the 1st Inventive Concept. If 

Dr Ratty and Dr Poo were the ones who had come up with the 1st Inventive Concept, there was no reason why Dr Poo could not have provided the details in his draft of the TEC Proposal, but had to leave them to Dr Sethi. On the stand, Dr Poo could not provide any satisfactory answer for why he 

did not fill in the details in the TEC Proposal, except to say that that “was a first draft” [note: 46]. 

75     In addition, the evidence was that on 16 February 2005, Dr Poo sent an email to Dr Sethi, where he requested Dr Sethi to “write down the 4 areas that you mentioned in our discussion last week for me in this email”. Dr Sethi replied just 12 minutes later with the following: 

 ATOMS 


 A Four-phased electronic approach to laboratory request order management: 

1\. Bedside pathology ordering by doctors and nurse practitioners for ward-in-patients. 

2\. Positive-patient identification 

3\. Bedside phlebotomy management 

_4. Electronic linkage between ATOMS and HIS (Hospital Information System) the LIS (Lab Information System)_ 

 [emphasis added] 

The email exchange as set out above gave me further reason to believe that it was Dr Sethi, and not Dr Poo or Dr Ratty, who had come up with the 1st Inventive Concept, and that he had come up with it by early February 2005. 

76     In trying to prove that Dr Ratty and Dr Poo were the rightful inventors, Cicada relied primarily on a two-page handwritten note that Dr Ratty made during a meeting with NHG’s representative that was held on 1 February 2005. Dr Ratty said that the first page of the note contained the notes he had taken down when Dr Sethi explained, at the meeting, NUH’s existing infrastructure and the 

infrastructures that NUH was at that time developing (such as the CPOE) [note: 47]. He said that the second page of the note was the “manifestation” of his ideas in relation to ATOMS (which made him 

an inventor of the Invention), which he claimed he had come up with in late 2004 [note: 48]. At a small part on the second page of the handwritten note (there were other notes on the same page which Cicada was not relying on in the present matter), Dr Ratty had written the words “Order entry”. An arrow was drawn pointing away from these words to an unlabelled box, and this unlabelled box was in turn linked by a second arrow to a second box. The portion of the second page of the note that Cicada sought to rely on is reproduced below: 

Dr Ratty said that based on the above, one would be able to see that neither NUH nor Prof Sethi had any solutions to the problems caused by manual laboratory workflow, and Cicada said that the note “clearly show[ed] the concept, of a link between the front-end and back-end of test ordering and specimen processing”. I was not so persuaded. It was not sufficiently clear to me that the note showed the 1st Inventive Concept. 

77     While there was an absence of a single contemporaneous record that clearly showed a specific and definite point by which Dr Sethi came up with the 1st Inventive Concept, I was satisfied that this was done before the involvement of Dr Ratty and Dr Poo. In particular, for the reasons above, I was satisfied that the handwritten note, even if it did capture the 1st Inventive Concept, was after Dr Sethi formulated the idea of linking the various components. 


 Court: What was that you contributed that may be different than what Prof Sethi had? A: The part that we differ...would probably be the details, like materialising the graphical display, actually working out the SVM. 

_The 2nd Inventive Concept_ 

78     NUH did not, however, successfully discharge its burden of proving that it was Dr Sethi, and not Dr Ratty and/or Dr Poo, who had contributed to the 2nd Inventive Concept, that is, the specification for the taking of specimens, including how the system actually ensured identification or determination of the specimen requirements in each case, and the process of actual interaction or communication between different components of the system. The focus of the arguments and the evidence that was put before me was really elsewhere, particularly on whether the SVM was part of the Inventive Concept (which I decided was not), but not on who had contributed to the 2nd Inventive Concept. I therefore could not say that Dr Poo’s contribution in terms of coding what was required was not 

inventive or did not touch on the 2 nd Inventive Concept. As for Dr Ratty, his contribution was perhaps less tangible or apparent than Dr Poo’s (since Dr Poo was the one with the software 

engineering expertise [note: 49] ) but again I could not conclude that this contribution did not involve any invention or contribution to the 2nd Inventive Concept. 

79     In the circumstances, I concluded that Dr Sethi had come up with the 1st Inventive Concept, but that it was not disproved that Dr Ratty and Dr Poo had come up with the 2nd Inventive Concept. 

80     As for Peter Lim, I was not persuaded that he had contributed to either of the two inventive concepts. NUH’s case that Peter Lim was a co-inventor (together with Dr Sethi) rested primarily on its claim that it was Peter Lim who had come up with the SVM and the idea of the graphical display, and 

Peter Lim confirmed as such on the stand [note: 50] : 

81     Cicada disagreed that it was Peter Lim who had come up with the idea of the graphical display. This was, however, inconsequential, since given my conclusions (at [66]–[70] above) that the graphical display and the SVM were not part of the inventive concepts, the claim that Peter Lim was an inventor of the Invention could not succeed, even if we were to assume that he did contribute to these two aspects. Peter Lim might have made a contribution to the better functioning of the Invention, but his contribution was not to the inventive concepts. Dr Sethi’s evidence was that Peter Lim had worked closely with him in relation to the ATOMS project, but there was no evidence to suggest that he did more than what was suggested to him by Dr Sethi (putting aside the SVM and the idea of the graphical display). A person who merely did what was suggested to him by the actual deviser did not take part in devising the invention and could not be regarded as a joint inventor: see [53] above. 

**_Whether Dr Sethi was an employee of NUH at the material time_** 

82     Cicada contended that even if Dr Sethi was an inventor of the Invention, he was not an employee of NUH at the material time, and so NUH was not the proper plaintiff in the present matter. NUH maintained that Dr Sethi was its employee at the time he came up with the Invention; he was employed both as a Senior Consultant as well as the Chief of the Department of Laboratory Medicine 

at NUH [note: 51]. 

83     As mentioned (see [49] above), the circumstances under which an employer would have 


ownership of an employee’s invention was set out in s 49 of the Patents Act. Put another way, even if Dr Sethi was an inventor or co-inventor (as I had so found), in order for NUH’s current claim to succeed, it had to prove that all elements of s 49 were satisfied, _ie_ , that: 

 (a) Dr Sethi was NUH’s employee at the time that he came up with the Invention; and 

 either 

 (b) (i) the Invention was made in the course of Dr Sethi’s normal duties as an employee of NUH, or in the course of duties falling outside his normal duties but specifically assigned to him; and 

 (ii) the circumstances in either of the above cases were such that an invention might reasonably be expected to result from the carrying out of his duties; 

 or 

 (c) (i) the Invention was made in the course of the duties of Dr Sethi as the employee of NUH; and 

 (ii) at the time of making the invention, because of the nature of his duties and the particular responsibilities arising from the nature of his duties, he had a special obligation to further the interests of NUH’s undertaking. 

I would emphasise that even in the absence of opposition by Cicada, the onus was on NUH, as the claimant, to prove the above elements on a balance of probabilities. 

84     There was no single, general test that was determinative of whether a person was an employee of another, or was a mere contractor or supplier for services. Much would depend on the circumstances of each case. However, the court could take guidance in this analysis by considering the following non-exhaustive factors distilled from the authorities: 

 (a) Whether the work of the alleged employee was done as an integral part of the business of the alleged employer – “[U]nder a contract of service, a man is employed as a part of the business and his work is done as an integral part of the business: whereas under a contract for services his work, although done for the business, is not integrated into the business but is only accessory to it”: per Denning LJ in Stevenson, Jordan and Harrison Ltd v Macdonald and Evans [1952] 69 RPC 10 at 22. 

 (b) Whether the alleged employee was paid a regular salary or commission – A person who was remunerated through a regular salary rather than commission was more likely to be considered an employee: Ravi Chandran, Employment Law in Singapore , (LexisNexis, 4th Ed, 2014) (“ Employment Law ”) at [1.25], citing Kuala Lumpur Mutual Fund Berhad v J Bastian Leo & Anor [1988] 2 MLJ 526 (“ Bastian Leo ”). 

 (c) Whether there were stipulations as to working hours – A person who was subject to working hours was more likely to be considered an employee: Employment Law at [1.28], citing Bastian Leo. 

 (d) Whether the alleged employee was entitled to overtime pay – A person who was not an employee was less likely to get overtime pay: Employment Law at [1.29]. 


 (e) Whether the alleged employer contributed to the Central Provident Fund (“CPF”) account of the alleged employee – A person who made and obtained CPF contributions was more likely to be an employee: Employment Law at [1.30]. 

 (f) Whether the alleged employee was entitled to leave and holidays – An employee was more likely to be contractually entitled to leave and holidays: Kureoka Enterprise Pte Ltd v Central Provident Fund Board <span class="citation">[1992] SGHC 113</span> (“ Kureoka ”). 

 (g) Whether the alleged employee was entitled to medical leave – A person who was contractually entitled to medical leave and related benefits was more likely to be an employee: Kureoka. 

 (h) Whether the alleged employer had the power to dismiss the alleged employee from his service – If an employer was contractually entitled to terminate the services of a person with notice or salary in lieu of notice, it was more likely that an employment relationship exists: Chew Swee Hiang v Attorney-General and another <span class="citation">[1990] 2 SLR(R) 215</span> at [43]. 

85     As proof that Dr Sethi was its employee at the time that he came up of the Invention, NUH produced a letter dated 6 June 2002 titled “NUH Appointment” and a letter dated 10 June 2005 titled “Renewal of Chiefship Appointment”. Cicada took issue that: 

 (a) The letters were titled with the word “appointment”, and not “employment”. 

 (b) Under the 6 June 2002 letter, Dr Sethi was to receive an allowance, and not salary, for his appointment at NUH. 

 (c) The fact that Dr Sethi’s appointment at NUH was tied to his position as an employee of NUS. The last sentence of the first paragraph of the 28 June 2005 letter stated that Dr Sethi’s appointment at NUH would lapse when his NUS appointment lapsed. 

On the basis of the above, as well as another letter dated 14 April 1986 that stated that Dr Sethi had been “deployed” from NUS to NUH as a Resident, Cicada argued that Dr Sethi was an employee of 

NUS at the material time of the Invention, and not of NUH [note: 52]. 

86     In the overall analysis, I was satisfied that Dr Sethi was an employee of NUH, rather than a mere contractor or supplier of services to NUH, at the material time when he came up with the 1st Inventive Concept. While there was a contract between him and NUS, he was also in a contract of employment with NUH, and in respect of the activities in issue in the present case, he was answerable to the control and supervision of NUH. There were several considerations that led me to this conclusion. 

87     First, I attached little value to the 14 April 1986 letter relied upon by Cicada. That letter predated the Invention by nearly two decades, and could not be taken as determinative or dispositive of Dr Sethi’s employment status at the material time. Absent other evidence to show that Dr Sethi’s evidence remained static all those years, it was more probable than not that changes to employment and deployment would have occurred. 

88     Second, the use of the term “appointment” instead of “employment” in the letters mentioned at [85] above was not conclusive that Dr Sethi was not an employee of NUH. In _Kureoka_ , hostesses of a lounge were held to be employees of the owner of the lounge even though they were given letters of “appointment”. 


89     Third, I was of the view that Dr Sethi’s work as Chief of the Department of Laboratory Medicine at NUH was integral to the business of NUH. I accepted that with that appointment, Dr Sethi’s duties included having overall responsibility for the department’s clinical operations, operating procedures 

and workflow processes such as specimen collection for laboratory analysis or testing [note: 53]. Such duties seemed to me to by an integral part of NUH’s operations as a hospital, rather than just being accessory to such operations. 

90     Fourth, although Dr Sethi was paid a yearly allowance for his duties as Chief of NUH’s Department of Laboratory Medicine, I did not consider this factor, in and of itself, to be inconsistent with NUH’s submission that he was nonetheless an employee of NUH. Furthermore, even though Dr Sethi only received annual allowances for his duties as Chief of NUH’s Department of Laboratory 

Medicine, he was paid a monthly salary as Senior Consultant at NUH [note: 54]. 

91     Fifth, there was clear evidence that NUH made monthly contributions to Dr Sethi’s CPF account 

at the material time [note: 55]. I considered this to be a significant factor pointing towards the 

conclusion that Dr Sethi was in NUH’s employment [note: 56]. 

92     Sixth, the letters produced by NUH stated that NUH had the power to terminate Sethi’s services 

by giving a “notice or salary _in lieu_ of notice” [note: 57]. 

93     There was a host of other factors which further supported NUH’s case that Dr Sethi was its employee at the material time. For instance, Dr Sethi was required by NUH to report for work “punctually, according to your work schedule or roster”, and any absenteeism by him without 

authorisation was “subject to discipline” [note: 58]. Dr Sethi was also entitled to benefits such as 

medical leave, annual leave, and holidays [note: 59]. I did not think that it was particularly significant that Dr Sethi’s appointment at NUH appeared to be tied to his position as an employee of NUS. Even if his appointment at NUH was, as Cicada contended, “ancillary” and “secondary” to his employment at 

NUS [note: 60] , this was really irrelevant as what mattered in the current inquiry was whether Dr Sethi was an employee of NUH at the material time (whether it was an appointment that might be “ancillary” or “secondary” to his appointment at the NUS). 

94     I therefore concluded that Dr Sethi was in the employment of NUH at the time that he came up with the 1st Inventive Concept. It did not matter that at that time, concurrent with his contract of employment with NUH, there was also an employment contract between him and NUS. 

95     The matter did not, however, end here. Cicada submitted that even if the court found Dr Sethi to be NUH’s employee, he did not conceive the inventive concepts of the Invention during the course of his duties at NUH, and that in any event, the Invention could not reasonably be expected to result 

during the course of Dr Sethi’s normal duties [note: 61]. Cicada said that Dr Sethi’s duties as Senior 

Consultant would primarily be of a clinical nature which concerned the treatment of patients [note: 62] 

. He was not employed by NUH as an inventor or researcher and there were no express terms in Dr Sethi’s letters of appointment with NUH that imposed any contractual duty for him to research, 

innovate or invent for NUH [note: 63]. Cicada also submitted that as a hospital, the essential purpose of NUH (and by extension that of its employees) was to treat illness and diseases and not to develop 

technology that might assist in the treatment of patients [note: 64]. 

96     I was not so persuaded by Cicada. I was of the view that Dr Sethi did conceive the 1st Inventive Concepts in the course of his normal duties as the Chief of NUH’s Department of Laboratory 


Medicine, and that the circumstances were such that an invention might reasonably be expected to result from the carrying out of his duties. The letters of 6 June 2002 and 10 June 2005 provided that as Chief of NUH’s Department of Laboratory Medicine, he was to: 

 ... be accountable for the professional and administrative activities within your department in accordance with the hospital’s Mission and values... [and] maintain the highest standards in professional performance, teaching, research and developments of staff in your department... 

And it was NUH’s mission to provide: 

 ... personalised, specialised, accessible and cost-effective care of the highest quality within an environment of intensive research and excellent medical education [note: 65]. 

It was not disputed that prior to the Invention, there were problems in NUH’s existing processes for laboratory specimen collection and management that could compromise patient safety (see [11] above). I accepted that as the Chief of NUH’s Department of Laboratory Medicine, it was his duty to try to resolve such problems by looking to improve the hospital’s operations and workflow processes for the management of laboratory specimen collection, so as to maintain “the highest standards in professional performance of his department” and also to fulfil NUH’s mission to provide “care of the highest quality”. It was in the course of performing this duty that Dr Sethi came up with the 1st Inventive Concept. 

97     I was further of the view that although Dr Sethi was not employed by NUH as an inventor or researcher and there were no express terms in Dr Sethi’s letters of appointment with NUH that imposed any contractual duty for him to research, innovate or invent for NUH, the Invention was reasonably expected to result from his carrying out of his normal duties as Chief of the Department of Laboratory Medicine. The courts needed to recognise that there was a strong innovative role inherent in many jobs these days, even if it was not explicitly mentioned within the normal or day-to-day job scope. All employees, whether in the public or private sector, whether managerial or clerical, were expected to contribute to the organisation by proposing innovations or improvements. What counted as being within the scope of employment had to be seen in that light. 

98     Cicada then made a final submission that Dr Sethi was bound by NUS’ intellectual property policy that precluded NUH’s alleged entitlement to the Invention. The salient terms of NUS’ intellectual 

property policy are set out below [note: 66] : 

 D. Ownership of Intellectual Property 

1\. Subject to Rule G, all rights, title and interest in Intellectual Property _developed in the course or furtherance of University Research_ shall vest in and belong to the University. 

 ... 

3\. In addition, Intellectual Property developed in the following instances shall be deemed to be developed in the course of University Research: 

 (a) Intellectual Property developed by the University Member in fulfilment of his contract of employment as a staff member; 

 (b) Intellectual Property developed by the University Member for the purpose of commercial exploitation i f such Intellectual Property falls within the area of expertise of the University 


 Member for which he was hired by the University or is related to his duties as a University Member. 

 [emphasis added] 

99     In my view, this argument had little merit. The above provisions of NUS’ intellectual property policy were not attracted because Dr Sethi came up with the 1st Inventive Concept in his capacity as an employee of NUH, and not “in the course or furtherance of University Research” at NUS. Cicada contended that if Dr Sethi had come up with the Invention, he would be deemed to have come up with the Invention in the course of University Research in view of clause 3(b) above, provided that any intellectual property developed that fell “within the area of expertise of the University Member for which he was hired by the University or is related to his duties as a University Member” would be deemed as such. I could not accept this contention. Dr Sethi was engaged by NUS as a lecturer in 

the Department of Pathology [note: 67] ; he was engaged for this expertise in pathology and his duties were to teach subjects in this field. The Invention did not fall within this area of pathology. 

**Conclusion** 

100    In view of the above, I ordered that Dr Sethi, Dr Ratty and Dr Poo be named as joint inventors of the invention, and for NUH to be named as a joint proprietor of the Patent together with Cicada. I further awarded costs to NUH fixed at $77,500 and disbursements of $22,072.90. 

[note: 1] (^) Plaintiff’s Closing Submissions at [34]; Defendant’s Closing Submissions at [2]. [note: 2] (^) Dr Sethi’s affidavit dated 13 June 2016 at [4(2)]. [note: 3] (^) Plaintiff’s Closing Submissions at [77]; NE of 16 March 2016, p 102. [note: 4] (^) Plaintiff’s Closing Submissions at [37] – [41]; Dr Sethi’s1st affidavit at [10] – [11]. [note: 5] (^) Dr Sethi’s1st affidavit at [12]; Plaintiff’s Closing Submissions at [50]. [note: 6] (^) Dr Sethi’s1st affidavit at [15]. [note: 7] (^) Plaintiff’s Closing Submissions at [61]. [note: 8] (^) Plaintiff’s Closing Submissions at [63]; Defendant’s Closing Submissions at [20]. [note: 9] (^) Defendant’s Closing Submissions at [2]. [note: 10] (^) At [0001] of the Patent. [note: 11] (^) At [0002] – [0004] of the Patent. [note: 12] (^) At [0005] – [0007] of the Patent. [note: 13] (^) At [0014] – [0017] of the Patent. 


[note: 14] (^) Plaintiff’s Submissions for Validity of the OS Proceedings at [7]. [note: 15] (^) Plaintiff’s Submissions for Validity of the OS Proceedings at [8]. [note: 16] (^) Plaintiff’s Submissions for Validity of the OS Proceedings at [9]. [note: 17] (^) Plaintiff’s Submissions for Validity of the OS Proceedings at [11]. [note: 18] (^) Plaintiff’s Opening Statement at [73]; Plaintiff’s Closing Submissions at [23]. [note: 19] (^) Plaintiff’s Closing Submissions at [10]; Plaintiff’s Reply Submissions at [39]. [note: 20] (^) Plaintiff’s Closing Submissions at [57]. [note: 21] (^) Plaintiff’s Closing Submissions at [60]. [note: 22] (^) Dr Sethi’s 1st Affidavit dated 18 March 2015, Exhibit SS-2, at [16] [note: 23] (^) Dr Sethi’s 1 st Affidavit dated 18 March 2015, Exhibit SS-2, at [21] [note: 24] (^) Plaintiff’s Closing Submissions at [57]. [note: 25] (^) Defendant’s Closing Submissions at [107(a)], [166] and [275]. [note: 26] (^) Defendant’s Closing Submissions at [107(b)]. [note: 27] (^) Statutory Declaration of Dr Ratty at pg 2790 of the Plaintiff’s Bundle of Documents. [note: 28] (^) Dr Ratty’s 2 nd affidavit at [11] and [12]. [note: 29] (^) Dr Ratty’s 2nd affidavit at [13]; Defendant’s Closing Submissions at [47]. [note: 30] (^) Dr Ratty’s 2nd affidavit at [13]; Defendant’s Closing Submissions at [48]. [note: 31] (^) N/E Day 2 from Pg 27 line 22 to Pg 28 line 21. [note: 32] (^) Exhibits PL-2 and PL-3 to Peter Lim’s Statutory Declaration dated 11 March 2013 and [22] of the said Statutory Declaration, which appears as SS-3 (Pg 185 of Dr Sethi’s 1 st Affidavit. [note: 33] (^) Defendant’s Closing Submissions at [65]. [note: 34] (^) N/E Day 1 at Pg 61 lines 21 – 23. [note: 35] (^) N/E Day 1 at Pg 56 lines 5 – 9. [note: 36] (^) N/E Day 1 at Pg 58 lines 2 – 5. 


[note: 37] (^) N/E Day 1 at Pg 58 lines 22 – 25. [note: 38] (^) N/E Day 2 at Pg 38 lines 13 – 18. [note: 39] (^) N/E Day 2 at Pg 38 lines 2 – 12. [note: 40] (^) Plaintiff’s Closing Submissions at [42]. [note: 41] (^) Plaintiff’s Closing Submissions at [43]. [note: 42] (^) Plaintiff’s Submissions at [46] – [48]. [note: 43] (^) Dr Sethi’s 1 st Affidavit dated 18 March 2015, Exhibit SS-2, at [36]. [note: 44] (^) Plaintiff’s Submissions at [64]. [note: 45] (^) Plaintiff’s Core Bundle at Pg 63. [note: 46] (^) Notes of Evidence, Day 2, at Pg 86 lines 18-25. [note: 47] (^) Dr Ratty’s 1st Affidavit at [17]. [note: 48] (^) Dr Ratty’s 1 st Affidavit at [19]. [note: 49] (^) Dr Ratty’s 1st Affidavit at [20]. [note: 50] (^) Notes of Evidence, Day 2, at Pg 34 lines 5-9. [note: 51] (^) Plaintiff’s Submissions on Employment at [9]. [note: 52] (^) Defendant’s Closing Submissions at [12]. [note: 53] (^) Plaintiff’s Submissions on Employment at [10]. [note: 54] (^) Plaintiff’s Submissions on Employment at [11]. [note: 55] (^) Dr Sethi’s CPF statements for 2004 to 2007 at Pg 51-58 of his affidavit. [note: 56] (^) Plaintiff’s Submissions on Employment at [14]. [note: 57] (^) Plaintiff’s Submissions on Employment at [17]. [note: 58] (^) Plaintiff’s Submissions on Employment at [12]. [note: 59] (^) Plaintiff’s Submissions on Employment at [15] and [16]. 


[note: 60] (^) Defendant’s Submissions (Employment) at [32] and [35]. [note: 61] (^) Defendant’s Submissions (Employment) at [41] and [42]. [note: 62] (^) Defendant’s Submissions (Employment) at [47]. [note: 63] (^) Defendant’s Submissions (Employment) at [48] and [60]. [note: 64] (^) Defendant’s Submissions (Employment) at [61]. [note: 65] (^) Plaintiff’s Submissions on Employment at [33] and [34]. [note: 66] (^) Dr Sethi’s affidavit dated 13 June 2016, p 91. [note: 67] (^) Defendant Submissions (Employment) at [80]. Copyright © Government of Singapore. 


Source: [link](https://www.singaporelawwatch.sg/Portals/0/Docs/Judgments/[2017] SGHC 53.pdf)
