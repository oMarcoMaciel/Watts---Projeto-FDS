describe('Adicionar Comodo', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Adicionar Comodo com sucesso', () => {
      // Navegar para a página de adicionar cômodo
      cy.get('[href="/addPontodeenergia/"]').click();
      cy.get('#locacao').select('Predio Boa Viagem');
      cy.get('#comodo').select('Sala');
      cy.get('#nome').type('Lg dual Inverter');
      cy.get('#gastos').type('22');
      cy.get('#quantidade').type('1');
      cy.get('button').click();
  
      
      // Verificar se a URL está correta após a submissão
      cy.url().should('eq', 'http://127.0.0.1:8000/');
    });
  });



