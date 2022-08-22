def VERSION = '2.1' // Version information not provided by tool on CLI

process GAMMA {
    tag "$meta.id"
    label 'process_low'
    //container 'staphb/gamma:2.1'
    container 'quay.io/jvhagey/gamma:2.1.5'

    input:
    tuple val(meta), path(fasta)
    path(db)

    output:
    tuple val(meta), path("*.gamma")                , emit: gamma
    tuple val(meta), path("*.psl")                  , emit: psl
    tuple val(meta), path("*.gff")  , optional:true , emit: gff
    tuple val(meta), path("*.fasta"), optional:true , emit: fasta
    path "versions.yml"                             , emit: versions

    when:
    task.ext.when == null || task.ext.when

    script:
    def args = task.ext.args ?: ''
    def prefix = task.ext.prefix ?: "${meta.id}"
    """
    db_name=\$(echo $db | sed 's:.*/::' | sed 's/.fasta//')
    if [[ ${fasta} == *.gz ]]
    then
        FNAME=\$(basename ${fasta} .gz)
        gunzip -f ${fasta}
        GAMMA.py \\
        $args \\
        \$FNAME \\
        $db \\
        ${prefix}_\$db_name
    else
        GAMMA.py \\
        $args \\
        $fasta \\
        $db \\
        ${prefix}_\$db_name
    fi

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        gamma: $VERSION
    END_VERSIONS
    """
}
