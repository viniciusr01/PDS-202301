describe('Criar Conta', () => {

  it('Adicionar Conta', () => {
    cy.visit('http://localhost:3000/main?cpf=105754752147500336670')
    cy.wait(2000)


    cy.get('[cypress_teste=buttonReceita]').within(() => {
      cy.contains('+ Receita').click().then
      cy.wait(2000)
    })

    cy.get('[cypress_teste=valor_reais]').type('129.94')
    cy.get('[cypress_teste=data_transacao]').type('15-06-2000')
    cy.get('[cypress_teste=descricao_transacao]').type('Valor teste e2e receita')

    cy.get('[cypress_teste=button_confirmar_transation]').within(() => {
      cy.contains('Criar').click().then
      cy.wait(2000)
    })

    

   


  })
})


