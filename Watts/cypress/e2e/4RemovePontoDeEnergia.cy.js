describe('Remover Ponto de Energia', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Remover Ponto de Energia', () => {
        cy.get('form[action*="deletePontodeenergia"]').each(($form) => {
            cy.wrap($form).find('button').click();
            cy.wait(1000); // Aguarde um segundo para a página ser recarregada
            cy.reload(); // Recarrega a página para garantir que o elemento foi removido
        });
    });
});
