"""
DM Informatique
HACHET Alexandre, 833
"""

import sys
sys.setrecursionlimit(3000)

# Q1
def codage_26(t):
	"""
	Fonction qui encode un texte par une liste de chiffres
	Par exemple: "py" -> [15, 24]
	"""

	encoded = []
	for c in t:
		encoded.append(ord(c) - 97)
	return encoded

# Q2
def texte_26(e):
	"""
	Fonction qui decode une liste de chiffres vers un texte
	Par exemple: [15, 24] -> "py"
	"""

	return "".join(chr(ec + 97) for ec in e)

# Q3
def verifie(l):
	"""
	Fonction qui verifie que tous les elements d'une liste
	sont bien en compris dans l'intervalle [0,25]
	"""

	for e in l:
		if not (e >= 0 and e <= 25):
			return False
	return True

# Q4
def chiffrement_cesar(l, d):
	"""
	Fonction qui code un texte avec la methode cesar,
	à l'aide d'un décalage d
	"""

	return [(e+d)%26 for e in l]

# Q5
def frequences(l):
	"""
	Fonction qui calcul la fréquence d'apparition de 
	chaque chiffre appartenant a [0,25] d'une liste
	"""

	c = [0]*26
	for i in range(len(l)):
		c[l[i]] += 1
	return c

# Q6
def indice_max(l):
	"""
	Fonction qui retourne l'indice de l'élément le plus grand d'une liste
	"""

	m = 0
	for i in range(len(l)):
		m = i if l[i] > l[m] else m
	return m

# Q7
def dechiffrement_auto(l):
	"""
	Fonction qui déchiffre un texte encodé en trouvant le décalage
	"""

	d = indice_max(frequences(l)) - 4
	return [(e-d)%26 for e in l]

# Q8
"""
encodage de "becunfromage" avec la clé "jean" >> "kichwjrbvegr"
"""

# Q9
def chiffrement_vigenere(l, c):
	"""
	Fonction qui chiffre un mot avec une clé suivant la méthode de vigenere
	"""

	return [(l[i]+c[i%len(c)])%26 for i in range(len(l))]

# Q10
def pgcd(a, b):
	"""
	Fonction qui retourne le pgcd de deux entiers
	"""

	return a if b == 0 else pgcd(b, a%b)

# Q11
def pgcd_liste(l):
	"""
	Fonction qui retourne le pgcd de tous les elements d'une liste
	"""

	d = [pgcd(l[i], l[i+1]) for i in range(len(l) - 1)] if len(l) > 0 else [0]
	return d[0] if len(d) == 1 else pgcd_liste(d)

# Q12
def pgcd_des_distances_entre_repetitions(lc, i):
	"""
	Fonction qui retourne le pgcd de deux indices de deux chaines de caractères identiques
	"""

	d = 0
	for j in range(i+6, len(lc)-4):
		if lc[i:i+5] == lc[j:j+5]:
			d = pgcd(d, j-i)
	return d

# Q13
def longueur_de_la_cle(lc):
	"""
	Fonction qui retourne la longueur de la clé utiliser pour l'encodage
	"""

	d = []
	for i in range(len(lc)-4):
		d.append(pgcd_des_distances_entre_repetitions(lc, i))
	return pgcd_liste(d)

# Q14
def decodage_vigenere_auto(lc):
	"""
	Fonction qui retourne le message décodé sous forme de liste de chiffre appartenant a [0,25]
	"""
	c, k = [], longueur_de_la_cle(lc)
	for i in range(0, k):
		c.append(indice_max(frequences(lc[i:len(lc):k])) - 4)

	return [(lc[i]-c[i%len(c)])%26 for i in range(len(lc))]

## Petits tests 

exemple_cesar = chiffrement_cesar([11, 24, 2, 4, 4, 12, 0, 18, 18, 4, 13, 0], 12)
exemple1 = chiffrement_vigenere([11, 24, 2, 4, 4, 12, 0, 18, 18, 4, 13, 0], [18, 20, 15])
exemple2 = chiffrement_vigenere([11, 24, 2, 4, 4, 12, 0, 18, 18, 4, 13, 0], [12, 0, 19, 7, 18])

## Quelques exemples de textes un peu longs sur lesquels appliquer Vigenere 

texte1 = 'lesmathematiquesoulamathematiquesontunensembledeconnaissancesabstraitesresultantderaisonnementslogiquesappliquesadesobjetsdiverstelsquelesnombreslesformeslesstructuresetlestransformationsellessontaussiledomainederecherchedeveloppantcesconnaissancesainsiqueladisciplinequilesenseigneellespossedentplusieursbranchestellesquelarithmetiquelalgebrelanalyselageometrielalogiquemathematiqueetcilexisteegalementunecertaineseparationentrelesmathematiquespuresetlesmathematiquesappliqueeslesmathematiquessedistinguentdesautressciencesparunrapportparticulieraureelcarlobservationetlexperiencenesyportentpassurdesobjetsphysiquesellessontdenatureentierementintellectuellefondeessurdesaxiomesdeclaresvraisousurdespostulatsprovisoirementadmiscesaxiomesenconstituentlesfondementsetnedependentdoncdaucuneautrepropositionunenoncemathematiquedenommegeneralementapresetrevalidetheoremepropositionlemmefaitscholieoucorollaireestconsiderecommevalidelorsquelediscoursformelquietablitsaveriterespecteunecertainestructurerationnelleappeleedemonstrationouraisonnementlogicodeductifunenoncepresentecommeplausiblemaisquinapasencoreeteetablicommevraidemontreenlangageutiliseparlesmathematicienssappelleuneconjecture'

texte_chiffre1=codage_26(texte1)
cle1=codage_26("massena")
#a decommenter quand vous aurez ecrit la fonction !
texte_code1=chiffrement_vigenere(texte_chiffre1, cle1)

texte2='donaldervinknuthnelejanvieramilwaukeeauwisconsinestuninformaticienetmathematicienamericainderenometprofesseuremeriteeninformatiquealuniversitestanfordetatsunisentantqueprofesseuremeritedelartdeprogrammerilestundespionniersdelalgorithmiqueetafaitdenombreusescontributionsdansplusieursbranchesdelinformatiquetheoriqueilestlauteurdunecentainedarticlesetdunedizainedelivressurlalgorithmiqueetlesmathematiquesdiscreteslespremiersvolumesaveclapartiedejapublieeduvolumeadetheartofcomputerprogrammingtaocpdemeurentdesouvragesdereferencecequiestexceptionneldansunesciencecommelinformatiquequievoluetresrapidementafindavoirunebonnequalitedemiseenpagepourladeuxiemeeditiondesontaocpknuthacreedeuxlogicielslibresparlasuitelargementutilisesentypographieprofessionnelleetenmathematiquestexetmetafontsoninteretpourlatypographielaegalementpousseacreerlapolicecomputermodernpolicepardefautdetex'

texte_chiffre2=codage_26(texte2)
cle2=codage_26("svartz")
#a decommenter quand vous aurez ecrit la fonction !
texte_code2=chiffrement_vigenere(texte_chiffre2, cle2)

texte3='latheierederussellparfoisappeleetheierecelesteestuneanalogieevoqueeparbertrandrussellpourcontesterlideequecestausceptiquederefuterlesbasesinverifiablesdelareligionetpouraffirmerquecestplutotaucroyantdelesprouverlideeestunehypothetiquetheiereenorbiteautourdusoleilentrelaterreetlaplanetemarsselonrussellycroireetdemanderauxgensdycroiresouspretextequilnestpaspossibledeprouversanonexistenceestinsenselatheierederussellestuneillustrationdurasoirdockhamleconceptdelatheierederussellaeteextrapoleaucomiqueplusparticulierementautraversdelalicorneroseinvisibledumonstreenspaghettisvolantetduculteducanardenplastiquejaunedeleobassidansunarticleintituleisthereagodecritpourunnumerodelillustratedmagazinedemaisquinefutjamaispubliebertrandrussellecrivaitdenombreusespersonnesorthodoxesparlentcommesicetaitletravaildessceptiquesderefuterlesdogmesplutotquaceuxquilessoutiennentdelesprouverceciestbienevidemmentuneerreursijesuggeraisquentrelaterreetmarssetrouveunetheieredeporcelaineenorbiteelliptiqueautourdusoleilpersonneneseraitcapabledeprouverlecontrairepourpeuquejaieprislaprecautiondepreciserquelatheiereesttroppetitepouretredetecteeparnospluspuissantstelescopesmaissijaffirmaisquecommemapropositionnepeutetrerefuteeilnestpastolerablepourlaraisonhumainedendouteronmeconsidereraitaussitotcommeunilluminecependantsilexistencedecettetheiereetaitdecritedansdeslivresanciensenseigneecommeuneveritesacreetouslesdimanchesetinculqueeauxenfantsalecolealorstoutehesitationacroireensonexistencedeviendraitunsignedexcentriciteetvaudraitausceptiquelessoinsdunpsychiatreauneepoqueeclaireeoudelinquisiteurendestempsplusanciens'

texte_chiffre3=codage_26(texte3)
cle3=codage_26("info")
#a decommenter quand vous aurez ecrit la fonction !
texte_code3=chiffrement_vigenere(texte_chiffre3, cle3)