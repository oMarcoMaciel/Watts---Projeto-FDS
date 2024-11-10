# Contribuindo para o Watts

Obrigado por considerar contribuir para o Watts! Aqui estão algumas diretrizes para ajudar você a configurar o ambiente e começar a contribuir.

## Requisitos

- Python 3.12
- Node.js e npm
- Git

## Configuração do Ambiente

1. **Clone o repositório:**

    ```sh
    git clone https://github.com/seu-usuario/Watts---Projeto-FDS.git
    cd Watts---Projeto-FDS
    ```

2. **Crie e ative um ambiente virtual:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. **Instale as dependências do Python:**

    ```sh
    cd Watts
    pip install -r requirements.txt
    ```

4. **Instale as dependências do Node.js:**

    ```sh
    npm ci
    ```

5. **Configure o banco de dados:**

    ```sh
    python manage.py migrate
    ```

6. **Execute o servidor localmente:**

    ```sh
    python manage.py runserver
    ```

7. **Execute os testes:**

    ```sh
    npx cypress run
    ```

## Contribuindo

1. **Crie uma nova branch para sua feature ou correção de bug:**

    ```sh
    git checkout -b minha-feature
    ```

2. **Faça suas alterações e commit:**

    ```sh
    git add .
    git commit -m "Descrição das minhas alterações"
    ```

3. **Envie suas alterações para o repositório remoto:**

    ```sh
    git push origin minha-feature
    ```

4. **Abra um Pull Request no GitHub.**

   Após enviar suas alterações para o repositório remoto, acesse o GitHub e navegue até a seção de Pull Requests do projeto. Clique em "New Pull Request" e selecione a sua branch. Adicione uma descrição clara das suas mudanças, incluindo o propósito da contribuição e quaisquer detalhes adicionais que possam ser úteis para a revisão. Após a revisão e aprovação, sua contribuição será integrada ao projeto principal.


## Código de Conduta

Este projeto adota um ambiente inclusivo e colaborativo. Esperamos que todos os colaboradores tratem uns aos outros com respeito, ajam com profissionalismo e contribuam de maneira construtiva. Assédio, discriminação e outras formas de comportamento inadequado não serão tolerados.

## Contato

Se você tiver alguma dúvida, sinta-se à vontade para entrar em contato com qualquer um dos desenvolvedores listados no [README.md](README.md).

Obrigado por contribuir!