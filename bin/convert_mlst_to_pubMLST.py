#!/usr/bin/env python

# In format that can be imported directly to python scripts

# # Function to look up correct pubmlst name for downloading
def gs_to_db(genus, species):
    specific_dict = { 'Acinetobacter baumannii': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Acinetobacter calcoaceticus': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Acinetobacter nosocomialis': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Acinetobacter pittii': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Acinetobacter seifertti': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Acinetobacter diijkhoorniae': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Aggregatibacter actinomycetemcomitans': 'Aggregatibacter actinomycetemcomitans',
                'Anaplasma phagocytophilum': 'Anaplasma phagocytophilum',
                'Aspergillus fumigatus': 'Aspergillus fumigatus',
                'Bacillus cereus': 'Bacillus cereus',
                'Bacillus licheniformis': 'Bacillus licheniformis',
                'Bacillus subtilis': 'Bacillus subtilis',
                'Bacteroides fragilis': 'Bacteroides fragilis',
                'Bartonella bacilliformis': 'Bartonella bacilliformis',
                'Bartonella henselae': 'Bartonella henselae',
                'Bartonella washoensis': 'Bartonella washoensis',
                'Brachyspira hampsonii': 'Brachyspira hampsonii',
                'Brachyspira hyodysenteriae': 'Brachyspira hyodysenteriae',
                'Brachyspira intermedia': 'Brachyspira intermedia',
                'Brachyspira pilosicoli': 'Brachyspira pilosicoli',
                'Burkholderia cepacia': 'Burkholderia cepacia complex',
                'Burkholderia cenocepacia': 'Burkholderia cepacia complex',
                'Burkholderia multivorans': 'Burkholderia cepacia complex',
                'Burkholderia vietnamiensis': 'Burkholderia cepacia complex',
                'Burkholderia pyrrocinia': 'Burkholderia cepacia complex',
                'Burkholderia stabilis': 'Burkholderia cepacia complex',
                'Burkholderia ambifaria': 'Burkholderia cepacia complex',
                'Burkholderia pseudomallei': 'Burkholderia pseudomallei',
                'Campylobacter concisus': 'Campylobacter concisus/curvus',
                'Campylobacter curvus': 'Campylobacter concisus/curvus',
                'Campylobacter fetus': 'Campylobacter fetus',
                'Campylobacter helveticus': 'Campylobacter helveticus',
                'Campylobacter hyointestinalis': 'Campylobacter hyointestinalis',
                'Campylobacter insulaenigrae': 'Campylobacter insulaenigrae',
                'Campylobacter jejuni': 'Campylobacter jejuni',
                'Campylobacter lanienae': 'Campylobacter lanienae',
                'Campylobacter lari': 'Campylobacter lari',
                'Campylobacter sputorum': 'Campylobacter sputorum',
                'Campylobacter upsaliensis': 'Campylobacter upsaliensis',
                'Candida albicans': 'Candida albicans',
                'Candida glabrata': 'Candida glabrata',
                'Candida krusei': 'Candida krusei',
                'Candida tropicalis': 'Candida tropicalis',
                'Candidatus Liberibacter': 'Candidatus Liberibacter solanacearun',
                'Carnobacterium maltaromaticum': 'Carnobacterium maltaromaticum',
                'Citrobacter freundii': 'Citrobacter freundii',
                'Clonorchis sinensis': 'Clonorchis sinensis',
                'Clostridioides difficile': 'Clostridioides difficile',
                'Clostridium botulinum': 'Clostridium botulinum',
                'Clostridium perfringens': 'Clostridium perfringens',
                'Clostridium septicum': 'Clostridium septicum',
                'Corynebacterium diphtheriae': 'Corynebacterium diphtheriae',
                'Cutibacterium acnes': 'Cutibacterium acnes',
                'Dichelobacter nodosus': 'Dichelobacter nodosus',
                'Enterobacter cloacae': 'Enterobacter cloacae',
                'Enterobacter asburiae': 'Enterobacter asburiae',
#                'Enterobacter hormaechei': 'Enterobacter hormaechei',
                'Enterobacter kobei': 'Enterobacter kobei',
                'Enterobacter luwigii': 'Enterobacter luwigii',
                'Enterobacter nimipressuralis': 'Enterobacter nimipressuralis',
                'Enterobacter mori': 'Enterobacter mori',
                'Enterococcus faecalis': 'Enterococcus faecalis',
                'Enterococcus faecium': 'Enterococcus faecium',
                'Escherichia coli': 'Escherichia coli#1,Escherichia coli#2',
                'Flavobacterium psychrophilum': 'Flavobacterium psychrophilum',
                'Gallibacterium anatis': 'Gallibacterium anatis',
                'Glaesserella parasuis': 'Glaesserella parasuis',
                'Haemophilus influenzae': 'Haemophilus influenzae',
                'Helicobacter cinaedi': 'Helicobacter cinaedi',
                'Helicobacter pylori': 'Helicobacter pylori',
                'Helicobacter suis': 'Helicobacter suis',
                'Kingella kingae': 'Kingella kingae',
                'Klebsiella aerogenes': 'Klebsiella aerogenes',
                'Klebsiella oxytoca': 'Klebsiella oxytoca',
                'Klebsiella pneumoniae': 'Klebsiella pneumoniae',
                'Kudoa septempunctata': 'Kudoa septempunctata',
                'Lactobacillus salivarius': 'Lactobacillus salivarius',
                'Listeria monocytogenes': 'Listeria monocytogenes',
                'Macrococcus canis': 'Macrococcus canis',
                'Macrococcus caseolyticus': 'Macrococcus caseolyticus',
                'Mammaliicoccus sciuri': 'Mammaliicoccus sciuri',
                'Mannheimia haemolytica': 'Mannheimia haemolytica',
                'Melissococcus plutonius': 'Melissococcus plutonius',
                'Moraxella catarrhalis': 'Moraxella catarrhalis',
                'Mycobacteroides abscessus': 'Mycobacteroides abscessus',
                'Mycoplasma agalactiae': 'Mycoplasma agalactiae',
                'Mycoplasma anserisalpingitidis': 'Mycoplasma anserisalpingitidis',
                'Mycoplasma bovis': 'Mycoplasma bovis',
                'Mycoplasma flocculare': 'Mycoplasma flocculare',
                'Mycoplasma gallisepticum': 'Mycoplasma gallisepticum#1,Mycoplasma gallisepticum#2',
                'Mycoplasma hominis': 'Mycoplasma hominis',
                'Mycoplasma hyopneumoniae': 'Mycoplasma hyopneumoniae',
                'Mycoplasma hyorhinis': 'Mycoplasma hyorhinis',
                'Mycoplasma iowae': 'Mycoplasma iowae',
                'Mycoplasma pneumoniae': 'Mycoplasma pneumoniae',
                'Mycoplasma synoviae': 'Mycoplasma synoviae',
                'Orientia tsutsugamushi': 'Orientia tsutsugamushi',
                'Ornithobacterium rhinotracheale': 'Ornithobacterium rhinotracheale',
                'Paenibacillus larvae': 'Paenibacillus larvae',
                'Pasteurella multocida': 'Pasteurella multocida#1,Pasteurella multocida#2',
                'Pediococcus pentosaceus': 'Pediococcus pentosaceus',
                'Photobacterium damselae': 'Photobacterium damselae',
                'Piscirickettsia salmonis': 'Piscirickettsia salmonis',
                'Porphyromonas gingivalis': 'Porphyromonas gingivalis',
                'Pseudomonas aeruginosa': 'Pseudomonas aeruginosa',
                'Pseudomonas fluorescens': 'Pseudomonas fluorescens',
                'Pseudomonas putida': 'Pseudomonas putida',
                'Riemerella anatipestifer': 'Riemerella anatipestifer',
                'Salmonella enterica': 'Salmonella enterica',
                'Saprolegnia parasitica': 'Saprolegnia parasitica',
                'Staphylococcus aureus': 'Staphylococcus aureus',
                'Staphylococcus chromogenes': 'Staphylococcus chromogenes',
                'Staphylococcus epidermidis': 'Staphylococcus epidermidis',
                'Staphylococcus haemolyticus': 'Staphylococcus haemolyticus',
                'Staphylococcus hominis': 'Staphylococcus hominis',
                'Staphylococcus lugdunensis': 'Staphylococcus lugdunensis',
                'Staphylococcus pseudintermedius': 'Staphylococcus pseudintermedius',
                'Stenotrophomonas maltophilia': 'Stenotrophomonas maltophilia',
                'Streptococcus agalactiae': 'Streptococcus agalactiae',
                'Streptococcus bovis': 'Streptococcus bovis/equinus complex (SBSEC)',
                'Streptococcus equinus': 'Streptococcus bovis/equinus complex (SBSEC)',
                'Streptococcus canis': 'Streptococcus canis',
                'Streptococcus dysgalactiae': 'Streptococcus dysgalactiae equisimilis',
                'Streptococcus gallolyticus': 'Streptococcus gallolyticus',
                'Streptococcus oralis': 'Streptococcus oralis',
                'Streptococcus pneumoniae': 'Streptococcus pneumoniae',
                'Streptococcus pyogenes': 'Streptococcus pyogenes',
                'Streptococcus suis': 'Streptococcus suis',
                'Streptococcus thermophilus': 'Streptococcus thermophilus,Streptococcus thermophilus#2',
                'Streptococcus uberis': 'Streptococcus uberis',
                'Streptococcus zooepidemicus': 'Streptococcus zooepidemicus',
                'Treponema pallidum': 'Treponema pallidum',
                'Trichomonas vaginalis': 'Trichomonas vaginalis',
                'Vibrio cholerae': 'Vibrio cholerae,Vibrio cholerae#2',
                'Vibrio parahaemolyticus': 'Vibrio parahaemolyticus',
                'Vibrio tapetis': 'Vibrio tapetis',
                'Vibrio vulnificus': 'Vibrio vulnificus',
                'Xylella fastidiosa': 'Xylella fastidiosa',
                'Yersinia pseudotuberculosis': 'Yersinia pseudotuberculosis',
                'Yersinia ruckeri': 'Yersinia ruckeri'
                }
    generic_dict = { 'Achromobacter': 'Achromobacter spp.',
               'Aeromonas': 'Aeromonas spp.',
               'Arcobacter': 'Arcobacter spp.',
               'Bordetella': 'Bordetella spp.',
               'Borrelia': 'Borrelia spp.',
               'Brachyspira': 'Brachyspira spp.',
               'Brucella': 'Brucella spp.',
               'Chlamydiales': 'Chlamydiales spp.',
               'Cronobacter': 'Cronobacter spp.',
               'Edwardsiella': 'Edwardsiella spp.',
               'Geotrichum': 'Geotrichum spp.',
               'Leptospira': 'Leptospira spp.,Leptospira spp.#2,Leptospira spp.#3',
               'Mycobacteria': 'Mycobacteria spp.',
               'Neisseria': 'Neisseria spp.',
               'Rhodococcus': 'Rhodococcus spp.',
               'Shewanella': 'Shewanella spp.',
               'Sinorhizobium': 'Sinorhizobium spp.',
               'Streptomyces': 'Streptomyces spp',
               'Taylorella': 'Taylorella spp.',
               'Tenacibaculum': 'Tenacibaculum spp.',
               'Ureaplasma': 'Ureaplasma spp.',
               'Vibrio': 'Vibrio spp.',
               'Wolbachia ': 'Wolbachia ',
               }
    print("Looking up Genus species:",genus,species)
    if str(genus+" "+species) in specific_dict:
        #f.write(specific_dict[args.genus+" "+args.species]+"\n")
        print(specific_dict[genus+" "+species])
    elif str(genus) in generic_dict:
        #f.write(generic_dict[args.genus]+"\n")
        print(generic_dict[genus])
    else:
        #f.write("No Match Found\n")
        print("No match found")

# Function to look up correct pubmlst name from mlst tool output
def convert(to_convert):
    standard_to_srst2 = {   'abaumannii': 'Acinetobacter baumannii#1',
            'abaumannii(Oxford)': 'Acinetobacter baumannii#1',
            'abaumannii(Pasteur)': 'Acinetobacter baumannii#2',
            'abaumannii_2': 'Acinetobacter baumannii#2',
            'achromobacter': 'Achromobacter spp.',
            'aeromonas': 'Aeromonas spp.',
            'aphagocytophilum': 'Anaplasma phagocytophilum',
            'arcobacter': 'Arcobacter spp.',
            'bbacilliformis': 'Bartonella bacilliformis',
            'bcc': 'Burkholderia cepacia complex',
            'bcereus': 'Bacillus cereus',
            'bhampsonii': 'Brachyspira hampsonii',
            'bhenselae': 'Bartonella henselae',
            'bhyodysenteriae': 'Brachyspira hyodysenteriae',
            'bintermedia': 'Brachyspira intermedia',
            'blicheniformis': 'Bacillus licheniformis',
            'bordetella': 'Bordetella spp.',
            'borrelia': 'Borrelia spp.',
            'bpilosicoli': 'Brachyspira pilosicoli',
            'bpseudomallei': 'Burkholderia pseudomallei',
            'brachyspira': 'Brachyspira spp.',
            'brucella': 'Brucella spp.',
            'bsubtilis': 'Bacillus subtilis',
            'bwashoensis': 'Bartonella washoensis',
            'campylobacter': 'Campylobacter jejuni',
            'cbotulinum': 'Clostridium botulinum',
            'cconcisus': 'Campylobacter concisus/curvus',
            'cdifficile': 'Clostridioides difficile',
            'cdiphtheriae': 'Corynebacterium diphtheriae',
            'cfetus': 'Campylobacter fetus',
            'cfreundii': 'Citrobacter freundii',
            'chelveticus': 'Campylobacter helveticus',
            'chlamydiales': 'Chlamydiales spp.',
            'chyointestinalis': 'Campylobacter hyointestinalis',
            'cinsulaenigrae': 'Campylobacter insulaenigrae',
            'clanienae': 'Campylobacter lanienae',
            'clari': 'Campylobacter lari',
            'cmaltaromaticum': 'Carnobacterium maltaromaticum',
            'cronobacter': 'Cronobacter spp.',
            'csepticum': 'Clostridium septicum',
            'csputorum': 'Campylobacter sputorum',
            'cupsaliensis': 'Campylobacter upsaliensis',
            'dnodosus': 'Dichelobacter nodosus',
            'ecloacae': 'Enterobacter cloacae',
            'ecoli': 'Escherichia coli#1',
            'ecoli(Achtman)': 'Escherichia coli#1',
            'ecoli(Pasteur)': 'Escherichia coli#2',
            'ecoli_2': 'Escherichia coli#2',
            'edwardsiella': 'Edwardsiella spp.',
            'efaecalis': 'Enterococcus faecalis',
            'efaecium': 'Enterococcus faecium',
            'fpsychrophilum': 'Flavobacterium psychrophilum',
            'ganatis': 'Gallibacterium anatis',
            'hcinaedi': 'Helicobacter cinaedi',
            'hinfluenzae': 'Haemophilus influenzae',
            'hparasuis': 'Glaesserella parasuis',
            'hpylori': 'Helicobacter pylori',
            'hsuis': 'Helicobacter suis',
            'kaerogenes': 'Klebsiella aerogenes',
            'kkingae': 'Kingella kingae',
            'koxytoca': 'Klebsiella oxytoca',
            'kpneumoniae': 'Klebsiella pneumoniae',
            'leptospira': 'Leptospira spp.',
            'leptospira_2': 'Leptospira spp.#2',
            'leptospira_3': 'Leptospira spp.#3',
            'liberibacter': 'Candidatus Liberibacter solanacearun',
            'lmonocytogenes': 'Listeria monocytogenes',
            'lsalivarius': 'Lactobacillus salivarius',
            'mabscessus': 'Mycobacteroides abscessus',
            'magalactiae': 'Mycoplasma agalactiae',
            'mbovis': 'Mycoplasma bovis',
            'mcanis': 'Macrococcus canis',
            'mcaseolyticus': 'Macrococcus caseolyticus',
            'mcatarrhalis': 'Moraxella catarrhalis',
            'mflocculare': 'Mycoplasma flocculare',
            'mhaemolytica': 'Mannheimia haemolytica',
            'mhyopneumoniae': 'Mycoplasma hyopneumoniae',
            'mhyorhinis': 'Mycoplasma hyorhinis',
            'miowae': 'Mycoplasma iowae',
            'mmassiliense': 'DO NOT USE',
            'mplutonius': 'Melissococcus plutonius',
            'mpneumoniae': 'Mycoplasma pneumoniae',
            'msynoviae': 'Mycoplasma synoviae',
            'mycobacteria': 'Mycobacteria spp.',
            'neisseria': 'Neisseria spp.',
            'orhinotracheale': 'Ornithobacterium rhinotracheale',
            'otsutsugamushi': 'Orientia tsutsugamushi',
            'pacnes': 'Cutibacterium acnes',
            'paeruginosa': 'Pseudomonas aeruginosa',
            'pdamselae': 'Photobacterium damselae',
            'pfluorescens': 'Pseudomonas fluorescens',
            'pgingivalis': 'Porphyromonas gingivalis',
            'plarvae': 'Paenibacillus larvae',
            'pmultocida_multihost': 'Pasteurella multocida#2',
            'pmultocida_rirdc': 'Pasteurella multocida#1',
            'ppentosaceus': 'Pediococcus pentosaceus',
            'pputida': 'Pseudomonas putida',
            'psalmonis': 'Piscirickettsia salmonis',
            'ranatipestifer': 'Riemerella anatipestifer',
            'rhodococcus': 'Rhodococcus spp.',
            'sagalactiae': 'Streptococcus agalactiae',
            'saureus': 'Staphylococcus aureus',
            'sbsec': 'Streptococus bovis, Strptococcus equinus',
            'scanis': 'Streptococcus canis',
            'sdysgalactiae': 'Streptococcus dysgalactiae equisimilis',
            'senterica': 'Salmonella enterica',
            'sepidermidis': 'Staphylococcus epidermidis',
            'sgallolyticus': 'Streptococcus gallolyticus',
            'shaemolyticus': 'Staphylococcus haemolyticus',
            'shominis': 'Staphylococcus hominis',
            'sinorhizobium': 'Sinorhizobium spp.',
            'slugdunensis': 'Staphylococcus lugdunensis',
            'smaltophilia': 'Stenotrophomonas maltophilia',
            'soralis': 'Streptococcus oralis',
            'spneumoniae': 'Streptococcus pneumoniae',
            'spseudintermedius': 'Staphylococcus pseudintermedius',
            'spyogenes': 'Streptococcus pyogenes',
            'ssuis': 'Streptococcus suis',
            'sthermophilus': 'Streptococcus thermophilus',
            'sthermophilus_2': 'Streptococcus thermophilus#2',
            'streptomyces': 'Streptomyces spp',
            'suberis': 'Streptococcus uberis',
            'szooepidemicus': 'Streptococcus zooepidemicus',
            'taylorella': 'Taylorella spp.',
            'tenacibaculum': 'Tenacibaculum spp.',
            'tpallidum': 'Treponema pallidum',
            'ureaplasma': 'Ureaplasma spp.',
            'vcholerae': 'Vibrio cholerae',
            'vcholerae2': 'Vibrio cholerae#2',
            'vibrio': 'Vibrio spp.',
            'vparahaemolyticus': 'Vibrio parahaemolyticus',
            'vtapetis': 'Vibrio tapetis',
            'vvulnificus': 'Vibrio vulnificus',
            'wolbachia': 'Wolbachia',
            'xfastidiosa': 'Xylella fastidiosa',
            'yersinia': 'Yersinia pseudotuberculosis',
            'ypseudotuberculosis': 'Yersinia pseudotuberculosis',
            'yruckeri': 'Yersinia ruckeri',
            }
    print("Looking to convert:",to_convert)
    if str(to_convert) in standard_to_srst2:
        print(standard_to_srst2[to_convert])
        return standard_to_srst2[to_convert]
    else:
        print("No match found")
        return "No match found"
