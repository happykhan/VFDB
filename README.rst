VFDB
====

The virulence factor/regions of interest databases used in the ST131 project.

MANIFEST:
    * ALL_FEATURES.fa (concatenation of all unique features)
    * Antibiotics.fa (bla-CTX-M-1 for CTX-15)
    * Antibiotics_CTX-15.fa
    * Autotransporters.fa (42). Based on Wells et al. (FIXED) 
    * Colicins_and_microcins.fa (21)
    * CU_fimbriae.fa (38). Based on  Wurpel et al. (FIXED)
    * fimB.fa (wt and IS)
    * Iron_uptake.fa (15) (FIXED)
    * Islands.fa (not if SeqFindR format, use chunk_mfa.py)
    * Islands_500bp_chunks.fa
    * O_antigen.fa (from Islands.fa)
    * Other_virulence_genes.fa (30)
    * plasmid_replicons.fa
    * Schembri_VFDB.fa (Autotransporters, Colicins_and_microcins, CU_fimbriae,
      Iron_uptake, Other_virulence_genes, Toxins, UPEC_specific_genes)
    * Toxins.fa (4) (FIXED)
    * UPEC_specific_genes.fa (125). Based on Mobley et al. (FIXED)

The following were duplicates across the pooled database:
    * c0393
    * c4308
    * c3610
    * c3619
    * c2436
    * c1374
    * c2482
    * c2775

**On the 07/06/2013 Mat Upton pointed out that there was an issues with some
sequences in the database. This was due to a bug in the KEGG extract script.**

The following databases are not effected:
    * Antibiotics.fa & Antibiotics_CTX-15.fa
    * Colicins_and_microcins.fa
    * fimB.fa
    * Islands.fa
    * Islands_500bp_chunks.fa
    * Other_virulence_genes.fa
    * O_antigen.fa
    * plasmid_replicons.fa


Suggested labels:
    * CU fimbriae
    * Autotransporters
    * Toxins
    * Iron uptake
    * Colicins and microcins
    * Other virulence genes
    * UPEC specific genes
