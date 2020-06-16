#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct node {
    int value;
    struct node* previous;
    struct node* next;
};

struct node* create_node(int value){
    struct node* new_node = (struct node*) malloc(sizeof(struct node));
    new_node->previous = NULL;
    new_node->next = NULL;
    new_node->value = value;
    return new_node;
}

struct list {
    struct node* front;
    int size;
};

struct list* create_list(){
    struct list* new_list = (struct list*) malloc(sizeof(struct list));
    new_list->front = NULL;
    new_list->size = 0;
    return new_list; 
}

void push(struct list* l, int value){
    struct node* new_node = create_node(value);
    if (l->front == NULL){
        new_node->previous = new_node;
        new_node->next = new_node;
        l->front = new_node;
    }
    else {
        new_node->previous = l->front->previous;
        new_node->next = l->front;
        l->front->previous->next = new_node;
        l->front->previous = new_node;
    }   
    l->size++;
}

void pop_value(struct list* l, int value){
    if (l->front != NULL){
        struct node* helper = l->front;
        while (helper != NULL && value != helper->value){
            helper = helper->next;
        }
        if (helper != NULL){
            helper->next->previous = helper->previous;
            helper->previous->next = helper-> next;
            free(helper);
            l->size--;
        }
    }
}

void pop_index(struct list* l, int index){
    if (l->size > index && index>0){
        struct node* helper = l->front;
        int i=0;
        if (index < l->size/2 ){
            while (i != index){
                helper = helper->next;
                i++;
            }
        }
        else {
            while (i != l->size - index){
                helper = helper->previous;
                i++;
            }
        }
        helper->next->previous = helper->previous;
        helper->previous->next = helper-> next;
        free(helper);
        l->size--;
    }
}

void print_list(struct list* l){
    struct node* helper = l->front;
    for(int i=0; i < l->size; i++){
        printf("%d ", helper->value);
        helper = helper->next;
    }
    printf("\n");
}

void fill_list(struct list* l){
    for(int i=0; i<1000; i++){
        int helper = rand();
        push(l, helper);
    }
}

struct list* merge_lists(struct list* l1, struct list* l2){
    if (l1->front == NULL) return l2;
    if (l2->front == NULL) return l1;
    l1->front->previous->next = l2->front;
    l2->front->previous->next = l1->front;
    l2->front->previous = l1->front;
    l1->front->previous = l2->front;
    l1->size += l2->size;
    return l1;
}

int get_by_id(struct list* l, int index){
    if (l->size > index && index>0){
        struct node* helper = l->front;
        int i=0;
        if (index < l->size/2 ){
            while (i != index){
                helper = helper->next;
                i++;
            }
        }
        else {
            while (i != l->size - index){
                helper = helper->previous;
                i++;
            }
        }
        return helper->value;
    }
    return -1;

}

void measure_time(struct list* l){
    int const_index = rand()%l->size;
    int var_index;
    clock_t time_period = clock();
    for (int i=0; i<1000; i++){
       get_by_id(l, const_index);
    }
    time_period = clock() - time_period;
    printf("Sredni czas dostepu do tego samego elementu: %lf ms\n", (double) time_period/CLOCKS_PER_SEC*1000);
    time_period = clock();
    for(int i=0; i<1000; i++){
        var_index = rand()%l->size;
        get_by_id(l, var_index);
    }
    time_period = clock() - time_period;
    printf("Sredni czas dostepu do losowego elementu: %lf ms\n", (double)time_period/CLOCKS_PER_SEC*1000);

}

int main(void){
    srand(time(0));
    struct list* my_list1 = create_list();
    struct list* my_list2 = create_list();
    fill_list(my_list1);
    fill_list(my_list2);
    measure_time(my_list1);
    merge_lists(my_list1, my_list2);
}