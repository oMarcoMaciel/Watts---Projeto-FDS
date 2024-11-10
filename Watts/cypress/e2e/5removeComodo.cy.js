describe('Remover Cômodo', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Remover Cômodo', () => {
        cy.get('form[action*="deleteComodo"]').each(($form, index, $list) => {
            cy.wrap($form).find('button').click().then(() => {
                if (index < $list.length - 1) {
                    cy.wait(1000); // Aguarde um segundo para a página ser recarregada
                    cy.reload(); // Recarrega a página para garantir que o elemento foi removido
                }
            });
        });
    });
});