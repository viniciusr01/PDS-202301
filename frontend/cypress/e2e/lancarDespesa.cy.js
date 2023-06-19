describe('Lancar despesa', () => {

    it('Realziar o lançamento de despesa', () => {
      cy.visit('http://localhost:3000/main?cpf=105754752147500336670')
      cy.wait(2000)
  
  
      cy.get('[cypress_teste=buttonDespesa]').within(() => {
        cy.contains('+ Despesa').click().then
        cy.wait(2000)
      })
  
      cy.get('[cypress_teste=valor_reais]').type('158')
      cy.get('[cypress_teste=data_transacao]').type('2023-06-17')
      cy.get('[cypress_teste=descricao_transacao]').type('Valor Teste e2e despesa')
  
      cy.get('[cypress_teste=button_confirmar_transation]').within(() => {
        cy.contains('Criar').click().then
        cy.wait(2000)
      })
  
      cy.get('[cypress_teste=despesaCard]').within(() => {
        cy.contains('Despesas').click().then
        cy.wait(2000)
      }) 
      
      
      const textos = [];
  
      cy.get('[cypress_teste=descriacaoTransacaoDespesa]').each(($el) => {
        textos.push($el.text());
      }).then(() => {
        expect(textos).to.include('Valor Teste e2e despesa 1/1');
      });
  
  
      const valores = []
      
  
      cy.get('[cypress_teste=valorTransacaoDespesa]').each(($el) => {
        valores.push($el.text());
      }).then(() => {
        expect(valores).to.include('R$ 158');
      });
      
  
  
    })
  })
  
  
  