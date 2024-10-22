describe('Adicionar Comodo', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Adicionar Comodo com sucesso', () => {
      // Navegar para a página de adicionar cômodo
      cy.get('[href="/addComodo/"]').click();
      cy.get('#nome').type('Sala');
      cy.get('#locacao').select('Predio Boa Viagem');
      cy.get('button').click();
  
      
      // Verificar se a URL está correta após a submissão
      cy.url().should('eq', 'http://127.0.0.1:8000/');
    });
  });