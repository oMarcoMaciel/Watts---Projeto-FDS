describe('Remover Comodo', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Remover Locação', () => {
        for (let i = 0; i < 3; i++) {
            
          cy.get(':nth-child(5) > :nth-child(1) > form > button').click();
        }
        
            
        
      });
    });