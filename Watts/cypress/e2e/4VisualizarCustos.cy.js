// cypress/e2e/4VisualizarCustos.cy.js

describe('Visualizar Custos', () => {
    beforeEach(() => {
      // Visita a página inicial antes de cada teste
      cy.visit('http://localhost:8000/');
    });
  
    it('Visualizar custo dos Pontos de Energia', () => {
        // Intercepta a requisição
        cy.intercept('/calcular_custo_ponto/**').as('calculoCustoPonto');
      
        // Clica no botão
        cy.contains('Pontos de Energia')
          .parent()
          .find('button')
          .contains('Custo do Ponto Mensal')
          .first()
          .click();
      
        // Aguarda a requisição terminar
        cy.wait('@calculoCustoPonto');
      
        // Verifica se o texto 'Custo do Ponto de Energia' aparece
        cy.contains('Custo do Ponto de Energia').should('be.visible');
      
        // Tarefa concluída
      });
  
    it('Visualizar custo dos Cômodos', () => {
      // Encontra e clica no botão "Calcular Custo Mensal" do primeiro cômodo
      cy.contains('Cômodos')
        .parent()
        .find('button')
        .contains('Custo do Cômodo Mensal')
        .first()
        .click();
  
      // Verifica se o texto 'Custo do Cômodo' aparece
      cy.contains('Custo do Cômodo').should('be.visible');
  
      // Tarefa concluída
    });
  
    it('Visualizar custo da Locação', () => {
      // Encontra e clica no botão "Calcular Custo Total" da primeira locação
      cy.contains('Locações')
        .parent()
        .find('button')
        .contains('Custo Total')
        .first()
        .click();
  
      // Verifica se o texto 'Custo da Locação' aparece
      cy.contains('Custo da Locação').should('be.visible');
  
      // Tarefa concluída
    });
  });