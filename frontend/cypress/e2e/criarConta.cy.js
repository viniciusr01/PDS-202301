describe('Criar Conta', () => {

  it('Adicionar Conta', () => {
    cy.visit('http://localhost:3000/main?cpf=105754752147500336670')
    cy.wait(2000)

    cy.get('[cypress_teste=buttonConta]').within(() => {
      cy.contains('+ Conta').click().then
      cy.wait(2000)
    })

    cy.get('[cypress_teste=nome_conta]').type('ContaTeste')
    cy.get('[cypress_teste=cor_conta]').type('FFFFF')
    cy.get('[cypress_teste=saldo_conta]').type('1000')


    cy.get('[cypress_teste=button_confirmar_conta]').within(() => {
      cy.contains('Criar').click().then
      cy.wait(2000)
    })

    cy.get('[cypress_teste=buttonReceita]').within(() => {
      cy.contains('+ Receita').click().then
      cy.wait(2000)
    })

    cy.get('[cypress_teste=placeConta]').within(() => {
      cy.contains('ContaTeste')
      cy.wait(2000)
    })

   


  })
})


