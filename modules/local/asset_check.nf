process ASSET_CHECK {
    label 'process_low'
    container 'quay.io/jvhagey/phoenix:base_v2.0.2'

    input:
    path(zipped_sketch)
    path(mlst_db_path)
    path(kraken_db)

    output:
    path('*.msh'),        emit: mash_sketch
    path("versions.yml"), emit: versions
    path('db'),           emit: mlst_db
    path('*_folder'),     emit: kraken_db

    when:
    task.ext.when == null || task.ext.when

    script:
    def container = task.container.toString() - "quay.io/jvhagey/phoenix:"
    """
    if [[ ${zipped_sketch} = *.gz ]]
    then
        pigz -vdf ${zipped_sketch}
    else
        :
    fi

    if [[ ${mlst_db_path} = *.tar.gz ]]
    then
        tar --use-compress-program="pigz -vdf" -xf ${mlst_db_path}
    else
        :
    fi

    if [[ ${kraken_db} = *.tar.gz ]]
    then
        folder_name=\$(basename ${kraken_db} .tar.gz)
        tar --use-compress-program="pigz -vdf" -xf ${kraken_db}
        mkdir \${folder_name}_folder
        mv *.kmer_distrib \${folder_name}_folder
        mv *.k2d \${folder_name}_folder
        mv seqid2taxid.map \${folder_name}_folder
        mv inspect.txt \${folder_name}_folder
        mv ktaxonomy.tsv \${folder_name}_folder
    else
        folder_name=\$(basename ${kraken_db} .tar.gz)
        mv \${folder_name} \${folder_name}_folder
    fi

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        phoenix_base_container: ${container}
    END_VERSIONS
    """
}
