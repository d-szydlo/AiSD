#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node* next;
};

struct node* create_node(int value){
    struct node* new_node = (struct node*) malloc(sizeof(struct node));
    new_node->next = NULL;
    new_node->value = value;
    return new_node;
}

struct queue {
    struct node* front;
    struct node* back;
};

struct queue* create_queue(){
    struct queue* new_queue = (struct queue*) malloc(sizeof(struct queue));
    new_queue->back = NULL;
    new_queue->front = NULL;
    return new_queue; 
}

void push(struct queue* q, int value){
    struct node* new_node = create_node(value);
    if (q->front == NULL){
        q->front = new_node;
        q->back = new_node;
    }
    else {
        q->back->next = new_node;
        q->back = new_node;
    }   
}

void pop(struct queue* q){
    if (q->front != NULL){
        q->front = q->front->next;
        if (q->front == NULL){
            q->back = NULL;
        }
    }
}

void print_queue(struct queue* q){
    struct node* helper = q->front;
    while (helper != NULL){
        printf("%d ", helper->value);
        helper = helper->next;
    }
    printf("\n");
}

int main(void){
    struct queue* my_queue = create_queue();
    push(my_queue, 1);
    push(my_queue, 2);
    push(my_queue, 3);
    print_queue(my_queue);
    pop(my_queue);
    print_queue(my_queue);
    pop(my_queue);
    pop(my_queue);
    print_queue(my_queue);
}