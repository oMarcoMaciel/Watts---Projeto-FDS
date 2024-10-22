describe('Remover Locação', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Remover Locação', () => {
        for (let i = 0; i < 2; i++) {
            
          cy.get(':nth-child(2) > :nth-child(1) > form > button').click();
        }
            
        
      });
    });