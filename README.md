# 🪐 Calculadora de Peso Planetário

Um projeto em Python que calcula como o peso de uma pessoa seria diferente em planetas e outros corpos celestes do Sistema Solar, usando fatores de gravidade relativos à Terra.

> Projeto desenvolvido para praticar fundamentos de Python, estruturas de repetição, dicionários, funções, validação de entrada e organização de código.

## ✨ Funcionalidades

- Calcula o peso informado na Terra em diferentes corpos celestes.
- Inclui Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano, Netuno e Lua.
- Valida valores menores ou iguais a zero.
- Trata entradas que não são numéricas.
- Exibe os resultados em uma tabela no terminal.
- Mantém os fatores de gravidade centralizados em uma constante.

## 🧮 Como funciona

O cálculo utiliza a relação:

```
peso_no_corpo_celeste = peso_na_Terra × fator_de_gravidade
```

Por exemplo, se uma pessoa informa **60 kg** e Marte possui um fator de aproximadamente **0,38**, o programa calcula:

```
60 × 0,38 = 22,80 kg
```

Os valores utilizados são fatores relativos à gravidade da Terra e representam uma simulação do peso equivalente em cada corpo celeste.

## 🛠️ Tecnologias

- **Python 3**
- Biblioteca padrão do Python
- Testes com **unittest**

## 📁 Estrutura do projeto

```
peso_planetas.py/
├── calculadora_planetas.py
├── tests/
│   └── test_calculadora_planetas.py
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/marcellabongiolo/peso_planetas.py.git
cd peso_planetas.py
```

### 2. Execute o programa

```bash
python calculadora_planetas.py
```

No Windows, caso o comando acima não funcione:

```bash
py calculadora_planetas.py
```

### 3. Informe seu peso

Digite seu peso na Terra em quilogramas quando solicitado.

## 🧪 Executando os testes

O projeto possui testes automatizados para verificar os cálculos e as validações de entrada.

```bash
python -m unittest discover -s tests -v
```

## 🌍 Corpos celestes

| Corpo celeste | Fator relativo à Terra |
|---|---:|
| Mercúrio | 0,38 |
| Vênus | 0,91 |
| Terra | 1,00 |
| Marte | 0,38 |
| Júpiter | 2,34 |
| Saturno | 0,93 |
| Urano | 0,92 |
| Netuno | 1,12 |
| Lua | 0,165 |

## 📚 Conceitos praticados

Este projeto trabalha conceitos importantes para quem está começando em desenvolvimento de software:

- Variáveis e constantes
- Dicionários
- Funções
- Estruturas de repetição
- Condicionais
- Tratamento de exceções
- Formatação de strings
- Type hints
- Testes automatizados
- Organização de projetos

## 👩‍💻 Autora

**Marcella Bongiolo**

Estudante de Engenharia de Software.

- GitHub: [@marcellabongiolo](https://github.com/marcellabongiolo)
- LinkedIn: [Marcella Bongiolo](https://www.linkedin.com/in/marcellabongiolo/)

## 📄 Licença

Este projeto está disponível sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.
