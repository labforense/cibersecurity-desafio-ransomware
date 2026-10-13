# Simulação Educacional de Criptografia de Arquivos

Projeto acadêmico em Python para demonstrar, **somente em ambiente controlado**, a criptografia e a recuperação de um arquivo fictício com AES em modo CTR. O repositório também documenta riscos, sinais e medidas defensivas para ransomware e keyloggers.

## Aviso ético e de segurança

Este material é exclusivamente educacional. Execute-o apenas em arquivos fictícios que você possua e dentro da pasta `lab_data/`. Não utilize estes scripts em documentos pessoais, sistemas de terceiros, ambientes corporativos ou qualquer contexto sem autorização explícita.

A simulação não possui propagação, persistência, ocultação, exfiltração, comunicação remota ou captura de teclado. Os scripts preservam o arquivo original e geram arquivos de saída separados, evitando indisponibilidade acidental.

## Objetivos

- Demonstrar criptografia simétrica AES com uma chave de 16 bytes.
- Observar a alteração de um arquivo de teste após a cifragem.
- Recuperar o conteúdo com a mesma chave.
- Relacionar o comportamento simulado aos impactos de ransomware reais.
- Registrar práticas de prevenção, detecção, resposta e recuperação.

## Estrutura

```text
.
├── encrypter.py
├── decrypter.py
├── requirements.txt
├── lab_data/
│   └── exemplo.txt
├── defesa/
│   └── medidas_de_prevencao.md
├── keylogger_demonstracao_segura/
│   └── README.md
└── images/
    └── .gitkeep
```

## Instalação

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instale a dependência:

```bash
python -m pip install -r requirements.txt
```

## Execução controlada

1. Leia o arquivo `lab_data/exemplo.txt`.
2. Execute `python encrypter.py`.
3. Confirme a criação de `lab_data/exemplo.txt.testeransomware`.
4. Observe que `lab_data/exemplo.txt` continua preservado.
5. Execute `python decrypter.py`.
6. Confira o resultado em `lab_data/exemplo.recuperado.txt`.

O script de criptografia é deliberadamente limitado ao arquivo de laboratório definido no código. O de recuperação também produz um novo arquivo, sem excluir a evidência cifrada.

## Como funciona

AES é uma cifra simétrica: a mesma chave é usada para cifrar e decifrar. Nesta demonstração, o fluxo é:

```text
exemplo.txt -> AES-CTR -> exemplo.txt.testeransomware
exemplo.txt.testeransomware -> AES-CTR -> exemplo.recuperado.txt
```

Em um incidente real, ransomware pode cifrar muitos arquivos e exigir pagamento. O pagamento não assegura recuperação e pode incentivar novos crimes; a estratégia adequada é prevenção, contenção, investigação e restauração a partir de backups verificados.

## Evidências sugeridas

Registre capturas em `images/` mostrando:

- A estrutura de arquivos do projeto.
- A instalação da dependência.
- O conteúdo original de `exemplo.txt`.
- A execução de `encrypter.py`.
- O arquivo cifrado criado.
- A execução de `decrypter.py`.
- A comparação entre o arquivo original e o recuperado.

## Defesa

Consulte `defesa/medidas_de_prevencao.md` para medidas de proteção contra ransomware. A documentação sobre keyloggers está em `keylogger_demonstracao_segura/README.md`.

## Autor

Marius Caff Rocha
