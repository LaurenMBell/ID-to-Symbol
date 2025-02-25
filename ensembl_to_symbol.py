import pandas as pd
from biomart import BiomartServer 

def ensembl_to_gene_symbol(ensembl_ids):
    #converts the given list of ensembl ids to gene symbols using the biomart database
    
    server = BiomartServer("http://www.ensembl.org/biomart")
    ensembl = server.datasets['hsapiens_gene_ensembl']
    results = ensembl.query(
        attributes=['ensembl_gene_id', 'hgnc_symbol'],
        filters={'ensembl_gene_id': ensembl_ids}
    )
    
    data = []
    for line in results.splitlines():
        fields = line.split("\t")
        if len(fields) == 2:
            ensembl_id, gene_symbol = fields
            if gene_symbol:
                data.append((ensembl_id, gene_symbol))
    
    return pd.DataFrame(data, columns=["Ensembl ID", "Gene Symbol"])

def to_file(gene_symbols_df, output_filename):
    #saves the gene symbols dataframe to a csv file
    
    gene_symbols_df.to_csv(output_filename)
    print(f"Gene symbols saved to {output_filename}")

if __name__ == '__main__':
    infile = input("Input filename with gene Ensembl IDs:\n")
    
    with open(infile) as infile:
        ensembl_ids = [line.strip() for line in infile]
    
    gene_symbols_df = ensembl_to_gene_symbol(ensembl_ids)
    
    print("Printing to terminal: \n")
    print(gene_symbols_df)
    
    outfile_path = input("Input output file name:\n")
    print("Saving to file: \n")
    to_file(gene_symbols_df, outfile_path)
