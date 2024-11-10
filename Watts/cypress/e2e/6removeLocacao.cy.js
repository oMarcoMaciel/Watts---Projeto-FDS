describe('Remover Locação', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Remover Locação', () => {
        cy.get('form[action*="deleteLocacao"]').each(($form) => {
            cy.wrap($form).find('button').click();
        });
    });
});