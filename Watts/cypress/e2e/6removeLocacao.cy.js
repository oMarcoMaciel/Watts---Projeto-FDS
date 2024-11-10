describe('Remover Locação', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Remover Locação', () => {
        cy.get('form[action*="deleteLocacao"]').each(($form) => {
            cy.wrap($form).find('button').click();
            cy.wait(1000); // Aguarde um segundo para a página ser recarregada
        });
    });
});