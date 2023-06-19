describe('Lancar receita', () => {

  it('Realziar o lançamento de receita', () => {
    cy.visit('http://localhost:3000/main?cpf=105754752147500336670')
    cy.wait(2000)


    cy.get('[cypress_teste=buttonReceita]').within(() => {
      cy.contains('+ Receita').click().then
      cy.wait(2000)
    })

    cy.get('[cypress_teste=valor_reais]').type('129')
    cy.get('[cypress_teste=data_transacao]').type('2023-06-17')
    cy.get('[cypress_teste=descricao_transacao]').type('Valor Teste e2e receita')

    cy.get('[cypress_teste=button_confirmar_transation]').within(() => {
      cy.contains('Criar').click().then
      cy.wait(2000)
    })

    cy.get('[cypress_teste=receitaCard]').within(() => {
      cy.contains('Receitas').click().then
      cy.wait(2000)
    }) 
    
    
    const textos = [];

    cy.get('[cypress_teste=descriacaoTransacao]').each(($el) => {
      textos.push($el.text());
    }).then(() => {
      expect(textos).to.include('Valor Teste e2e receita');
    });


    const valores = []
    

    cy.get('[cypress_teste=valorTransacao]').each(($el) => {
      valores.push($el.text());
    }).then(() => {
      expect(valores).to.include('R$ 129');
    });
    


  })
})


