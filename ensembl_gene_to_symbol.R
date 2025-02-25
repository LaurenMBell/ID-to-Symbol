library(biomaRt)

ensembl_to_symbol <- function(ensembl_ids) {
  ensembl <- useMart("ensembl")
  
  print(listDatasets(ensembl))
  dataset_name <- readline("What dataset do you want to use?\n Use hsapiens_gene_ensembl for human genes.")
  
  ensembl <- useDataset(dataset = dataset_name, mart = ensembl)
  
  results <- getBM(
    attributes = c("ensembl_gene_id", "hgnc_symbol"),
    filters = "ensembl_gene_id",
    values = ensembl_ids,
    mart = ensembl
  )
  
  return(results)
}
  
to_file <- function(gene_symbols_frame, outfile) { 
  write.csv(gene_symbols_frame, outfile)
  cat("saved to: ", outfile, "\n")
  }

infile <- readline("Input filename with gene Ensembl ID's:\n")
#infile <- "test.txt"

ensembl_ids <- readLines(infile)

gene_symbols_frame <- ensembl_to_symbol(ensembl_ids)

print(gene_symbols_frame)

outfile <- readline("Input what you want to name the output file:\n")
to_file(gene_symbols_frame, outfile)