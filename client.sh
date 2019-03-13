#!/bin/bash

# SERVER='chall2.imesec.ime.usp.br'
# PORT='7333'
SERVER='localhost'
PORT='7333'

function show_help() {
    cat <<-EOF 
Como usar: client COMANDO
Comandos disponíveis:
    help         - Mostra esse aviso.
    send ARQUIVO - Envia o arquivo de resposta para o servidor registrando como o TIME.
    
    O arquivo de resposta deve ser um arranjo das cidades do Texas
    explicitados no arquivo 'texas.txt' do desafio. Nota: Somente as
    cidades!

Exemplo do começo do arquivo:

Laredo
San_Antonio
Dallas
Austin
...
EOF
}

function build_json() {
    local current_json="{\"author\": \"$2\", \"cities\": ["
    local cities=$(awk '{ print "\""$0"\","}' "$1")
    current_json="$current_json$(echo $cities | sed 's/,$//g')"
    current_json="$current_json]}"
    
    echo "$current_json"
}

function send() {
    local endpoint='/check'
    local file="$1"
    if [ ! -f "$file" ]; then
        echo "O arquivo indicado não existe."
        echo
        show_help
        exit
    fi
    local json="$(build_json $file $agent)"

    curl -XPOST -d "$json" "$SERVER:$PORT$endpoint"
    echo
}

command="$1"

case "$command" in
send) send "$2" "$3" ;;
*) show_help ;;
esac
