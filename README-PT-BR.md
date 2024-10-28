
# Hublinker

Hublinker é uma ferramenta de linha de comando (CLI) para facilitar a navegação e o gerenciamento de repositórios no GitHub diretamente do terminal. Ideal para desenvolvedores que trabalham intensamente com GitHub e querem uma interface rápida e amigável para realizar operações comuns.


## Instalação
clone ou faça forque do projeto e vá para a pasta raiz

    
Baixando dependências
```bash
  pip install -r requirements.txt 
```

instalando projeto
(método recomendado pela dependencia)
```bash
  pip install .
```
ou a
```bash
  python3 setup.py install
```

caso queira rodar sem instalação utilize na pasta raiz do projeto
```bash
  python3 -m hublinker
```
## Documentação

- limit

lista o consumo e limit de uso da api do gitHub

```bash
    hublinker limit
```
- repos

grupo de comandos relacionados a repositórios

```bash
    hublinker repos
```

1) public

irá listar repositórios públicos de um usuário e permitirá fazer clone

```bash
    hublinker repos public --user <usuário>
```

1) private

irá listar seus repositórios privados através do token configurado e permitirá fazer clone

```bash
    hublinker repos private
```

- config

opções de configuração

```bash
    hublinker config
```

1) config set-token

adiciona o token para autenticação na api
(pode ser gerado em configurações -> configurações de desenvolvedor -> token de acesso pessoal -> tokens)

```bash
    hublinker config set-token
```

2) config set-clone-path

adiciona o caminho onde serão clonados novos repositórios

```bash
    hublinker config set-clone-path
```

3) config set-rows-page

altera o limit de linhas ao consultar repositórios

```bash
    hublinker config set-rows-page
```
## Contribuindo

Contribuições são bem-vindas! Para contribuir:
- Faça um fork do projeto

para features
- Crie uma nova branch (`git checkout -b feature/MinhaFeature`)
- Commit suas mudanças (`git commit -m 'Add MinhaFeature'`)
- Faça push para a branch (`git push origin feature/MinhaFeature`)
- Abra um Pull Request

para hotfix
- Crie uma nova branch (`git checkout -b hotfix/MeuHotFix_numeroIssue`)
- Commit suas mudanças (`git commit -m 'Add MeuHotFix_numeroIssue'`)
- Faça push para a branch (`git push origin hotfix/MeuHotFix_numeroIssue`)
- Abra um Pull Request

para bugFix
(adicione número da issue apenas se possuir se não adicione uma breve descrição)
- Crie uma nova branch (`git checkout -b bugFix/BugFix_numeroIssue`)
- Commit suas mudanças (`git commit -m 'Add BugFix_numeroIssue'`)
- Faça push para a branch (`git push origin bugFix/BugFix_numeroIssue`)

## Licença

[MIT](https://choosealicense.com/licenses/mit/)

