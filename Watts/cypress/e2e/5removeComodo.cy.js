describe('Remover Cômodo', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Remover Cômodo', () => {
        cy.get('form[action*="deleteComodo"]').each(($form) => {
            cy.wrap($form).find('button').click();
        });
    });
});