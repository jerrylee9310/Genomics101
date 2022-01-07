from numpy.core.fromnumeric import var
from numpy.ma.extras import notmasked_contiguous
from basic_tools import *
from pysam import VariantFile
import numpy as np
from sklearn import decomposition
import pandas as pd

# parsing vcf to matrix
genotypes = []
samples = []
variants_ids = []
with VariantFile(vcf_fn) as vcf_reader:
    cnt = 0
    for record in vcf_reader:
        cnt += 1
        if cnt % 100 == 0:
            samples = [sample for sample in record.samples]
            alleles = [record.samples[x].allele_indices for x in record.samples]
            genotypes.append(alleles)
            variants_ids.append(record.id)
        if cnt > 10000:
            break


genotypes = np.array(genotypes)
print(genotypes.shape) # (samples, variants, diploid)


# check 
matrix = np.count_nonzero(genotypes, axis=2).T
print(matrix.shape)

# PCA
pca = decomposition.PCA(n_components=2)
pca.fit(matrix)
print(pca.singular_values_)
to_plot = pca.transform(matrix)
print(to_plot.shape)

# print PCA values
df = pd.DataFrame(matrix, columns=variants_ids, index=samples)
df.to_csv('geno_mtx')