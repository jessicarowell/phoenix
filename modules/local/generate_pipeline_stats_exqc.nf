process GENERATE_PIPELINE_STATS_EXQC {
    tag "${meta.id}"
    label 'process_single'
    container 'quay.io/jvhagey/phoenix:base_v2.0.2'

    input:
    tuple val(meta), path(raw_qc), \
    path(fastp_total_qc), \
    path(srst_fullgenes_file), \
    path(kraken2_trimd_report), \
    path(krona_trimd), \
    path(kraken2_trimd_summary), \
    path(assembly_scaffolds), \
    path(filtered_assembly), \
    path(mlst_file), \
    path(gamma_HV), \
    path(gamma_AR), \
    path(gamma_replicon), \
    path(quast_report), \
    path(busco_specific_short_summary), \
    path(kraken2_asmbld_report), \
    path(krona_asmbld), \
    path(kraken2_asmbled_summary), \
    path(krona_weighted), \
    path(kraken2_weighted_report), \
    path(kraken2_weighted_summary), \
    path(taxID), \
    path(fastANI_formatted_file), \
    path(assembly_ratio_file), \
    path(amr_file), \
    path(gc_content)
    val(coverage)

    output:
    tuple val(meta), path('*.synopsis'), emit: pipeline_stats
    path("versions.yml")               , emit: versions

    script: // This script is bundled with the pipeline, in cdcgov/phoenix/bin/
    def prefix = task.ext.prefix ?: "${meta.id}"
    def raw             = raw_qc ? "-a $raw_qc" : "" // if raw_qc is null return "-a $raw_qc" else return ""
    def fastp_total     = fastp_total_qc ? "-b $fastp_total_qc" : ""
    def k2_trim_report  = kraken2_trimd_report ? "-e $kraken2_trimd_report" : ""
    def k2_trim_summary = kraken2_trimd_summary ? "-f $kraken2_trimd_summary" : ""
    def krona_trim      = krona_trimd ? "-g $krona_trimd" : ""
    def srst_file       = srst_fullgenes_file ? "-x $srst_fullgenes_file" : ""
    def container = task.container.toString() - "quay.io/jvhagey/phoenix:"
    """
    pipeline_stats_writer.sh \\
        $raw \\
        $fastp_total \\
        -c $gc_content \\
        -d ${prefix} \\
        $k2_trim_report \\
        $k2_trim_summary \\
        $krona_trim \\
        -h $assembly_scaffolds \\
        -i $filtered_assembly \\
        -j $kraken2_asmbld_report \\
        -k $kraken2_asmbled_summary \\
        -l $krona_asmbld \\
        -m $kraken2_weighted_report \\
        -n $kraken2_weighted_summary \\
        -o $krona_weighted \\
        -p $quast_report \\
        -q $taxID \\
        -r $assembly_ratio_file \\
        -s $busco_specific_short_summary \\
        -t $fastANI_formatted_file \\
        -u $gamma_AR \\
        -v $gamma_replicon \\
        -w $gamma_HV \\
        $srst_file \\
        -y $mlst_file \\
        -4 $amr_file \\
        -5 $coverage \\
        -3

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        phoenix_base_container: ${container}
    END_VERSIONS
    """
}
