describe('Remover Ponto de Energia', () => {
    beforeEach(() => {
      cy.visit('/');
    });
  
    it('Remover Ponto de Energia', () => {
       for (let i = 0; i < 2; i++) {
            
        cy.get(':nth-child(8) > :nth-child(1) > form > button').click();
   
      }
    
    });
  });
