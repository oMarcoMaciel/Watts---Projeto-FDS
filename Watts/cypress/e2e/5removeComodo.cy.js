describe('Remover Cômodo', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Remover Cômodo', () => {
        for (let i = 0; i < 3; i++) {
            
          cy.get(':nth-child(5) > :nth-child(1) > form > button').click();
        }
        
            
        
      });
    });