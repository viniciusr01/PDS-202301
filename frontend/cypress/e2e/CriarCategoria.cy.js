describe('Criar Categoria', () => {

  it('Criar Categoria de Produto', () => {
    cy.visit('http://localhost:3000/main?cpf=105754752147500336670')
    cy.wait(2000)

    cy.get('[cypress_teste=buttonCategoria]').within(() => {
      cy.contains('+ Categoria').click().then
      cy.wait(2000)
    })

    cy.get('[cypress_teste=nome]').type('CategoriaTesteCypress')
    cy.get('[cypress_teste=cor]').type('FFFFF')


    cy.get('[cypress_teste=buttonConfirmar]').within(() => {
      cy.contains('Criar').click().then
      cy.wait(2000)
    })

    cy.get('[cypress_teste=buttonReceita]').within(() => {
      cy.contains('+ Receita').click().then
      cy.wait(2000)
    })

    cy.get('[cypress_teste=placeCategory]').within(() => {
      cy.contains('CategoriaTesteCypress')
      cy.wait(2000)
    })

   


  })
})


